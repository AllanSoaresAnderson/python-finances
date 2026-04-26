from typing import Optional, List
from datetime import datetime

from domain.enum import TransactionCategory, FrequencyTransaction, VariableFrequencyTransaction
from domain.interfaces import TransactionRepository
from infrastructure.interfaces import DatabaseConnectionSqlLite
from src.domain.entities import Transaction


def _to_iso(dt: Optional[datetime]) -> Optional[str]:
    return dt.isoformat() if dt else None


def _from_iso(value: Optional[str]) -> Optional[datetime]:
    return datetime.fromisoformat(value) if value else None


def _map_row_to_entity(row) -> Transaction:
    frequency = row[5]
    variable_frequency = row[6]

    return Transaction(
        ident=row[0],
        name=row[1],
        category=TransactionCategory(row[2]),
        start_date=_from_iso(row[3]),
        value=row[4],
        frequency=FrequencyTransaction(frequency) if frequency else None,
        variable_frequency=VariableFrequencyTransaction(variable_frequency) if variable_frequency else None,
        variable_range=row[7],
        date_created=_from_iso(row[8]),
        date_updated=_from_iso(row[9]),
        deletion_date=_from_iso(row[10]),
        id_baggin=row[11],
        id_entity=row[12],
    )


class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self, database: DatabaseConnectionSqlLite):
        self.database = database

    def insert(self, transaction: Transaction) -> Transaction:
        sql = '''
              INSERT INTO transactions
              (name, 
               category, 
               start_date, 
               value, 
               frequency,
               variable_frequency,
               variable_range,
               date_created,
               date_updated,
               deletion_date,
               id_baggin,
               id_entity
              )
              VALUES (
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?, 
                         ?
                     ) 
              '''

        with self.database.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                sql,
                (
                    transaction.name,
                    transaction.category.value,
                    transaction.start_date.isoformat(),
                    str(transaction.value),
                    transaction.frequency.value if transaction.frequency else None,
                    transaction.variable_frequency.value if transaction.variable_frequency else None,
                    transaction.variable_range,
                    datetime.now().isoformat(),
                    datetime.now().isoformat(),
                    None,
                    transaction.id_baggin,
                    transaction.id_entity
                )
            )
            _id = cursor.lastrowid
            if cursor.rowcount != 1:
                raise Exception("Erro ao inserir Entity")

            connection.commit()

            if _id:
                transaction.id = _id

        return transaction

    def update(self, transaction: Transaction) -> None:
        sql = '''
              UPDATE transactions
              SET name          = ?, 
                  category    = ?, 
                  start_date          = ?,
                  value      = ?,
                  frequency   = ?,
                  variable_frequency = ?,
                  variable_range = ?,
                  date_updated = ?,
                  id_baggin      = ?,
                  id_entity      = ?
              WHERE id = ? 
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                transaction.name,
                transaction.category.value,
                transaction.start_date.isoformat(),
                transaction.value,
                transaction.frequency.value if transaction.frequency else None,
                transaction.variable_frequency.value if transaction.variable_frequency else None,
                transaction.variable_range,
                datetime.now().isoformat(),
                transaction.id_baggin,
                transaction.id_entity,
                transaction.id
            ))

            conn.commit()

    def find_by_id(self, transaction_id: int) -> Optional[Transaction]:
        sql = 'SELECT * FROM transactions WHERE id = ?'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (transaction_id,))
            row = cursor.fetchone()

            if not row:
                return None

            return _map_row_to_entity(row)

    # 🔹 FIND ALL
    def find_all(self) -> List[Transaction]:
        sql = 'SELECT * FROM transactions WHERE deletion_date IS NULL'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            return [_map_row_to_entity(row) for row in rows]


    def delete(self, transaction_id: int) -> None:
        sql = '''
              UPDATE transactions
              SET deletion_date = ?
              WHERE id = ? \
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                datetime.now().isoformat(),
                transaction_id
            ))
            conn.commit()

