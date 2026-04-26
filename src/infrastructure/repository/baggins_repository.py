from typing import Optional, List
from datetime import datetime
from domain.enum import TypeBaggins
from domain.interfaces import BagginsRepository
from infrastructure.interfaces import DatabaseConnectionSqlLite
from src.domain.entities import Baggins


def _to_iso(dt: Optional[datetime]) -> Optional[str]:
    return dt.isoformat() if dt else None


def _from_iso(value: Optional[str]) -> Optional[datetime]:
    return datetime.fromisoformat(value) if value else None


def _map_row_to_entity(row) -> Baggins:
    return Baggins(
        id=row[0],
        name=row[1],
        start_date=_from_iso(row[2]),
        type=TypeBaggins(row[3]),
        amount_time=row[4],
        date_created=_from_iso(row[5]),
        deletion_date=_from_iso(row[6]),
    )


class BagginsRepositoryImpl(BagginsRepository):
    def __init__(self, database: DatabaseConnectionSqlLite):
        self.database = database

    def insert(self, baggins: Baggins) -> Baggins:
        sql = '''
              INSERT INTO baggins
              (name, 
               start_date, 
               type, 
               amount_time, 
               date_created, 
               deletion_date)
              VALUES (?, ?, ?, ?, ?, ?) 
              '''

        with self.database.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                sql,
                (
                    baggins.name,
                    baggins.start_date.isoformat() if baggins.start_date else None,
                    baggins.type.value,
                    baggins.amount_time,
                    datetime.now().isoformat(),
                    baggins.deletion_date.isoformat() if baggins.deletion_date else None,
                )
            )
            _id = cursor.lastrowid
            if cursor.rowcount != 1:
                raise Exception("Erro ao inserir Baggins")

            connection.commit()

            if _id:
                baggins.id = _id

        return baggins

    def update(self, baggins: Baggins) -> None:
        sql = '''
              UPDATE baggins 
              SET name          = ?, 
                  start_date    = ?, 
                  type          = ?, 
                  amount_time   = ?, 
                  date_created  = ?, 
                  deletion_date = ?
              WHERE id = ? 
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                baggins.name,
                _to_iso(baggins.start_date),
                baggins.type.value,
                baggins.amount_time,
                _to_iso(baggins.date_created),
                _to_iso(baggins.deletion_date),
                baggins.id
            ))

            conn.commit()

    def find_by_id(self, baggins_id: int) -> Optional[Baggins]:
        sql = 'SELECT * FROM baggins WHERE id = ?'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (baggins_id,))
            row = cursor.fetchone()

            if not row:
                return None

            return _map_row_to_entity(row)

    # 🔹 FIND ALL
    def find_all(self) -> List[Baggins]:
        sql = 'SELECT * FROM baggins WHERE deletion_date IS NULL'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            return [_map_row_to_entity(row) for row in rows]


    def delete(self, baggins_id: int) -> None:
        sql = '''
              UPDATE baggins
              SET deletion_date = ?
              WHERE id = ? \
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                datetime.now().isoformat(),
                baggins_id
            ))
            conn.commit()

