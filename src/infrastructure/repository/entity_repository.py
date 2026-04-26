from typing import Optional, List
from datetime import datetime
from domain.enum import TypeBaggins
from domain.interfaces import EntityRepository
from infrastructure.interfaces import DatabaseConnectionSqlLite
from src.domain.entities import Entity


def _to_iso(dt: Optional[datetime]) -> Optional[str]:
    return dt.isoformat() if dt else None


def _from_iso(value: Optional[str]) -> Optional[datetime]:
    return datetime.fromisoformat(value) if value else None


def _map_row_to_entity(row) -> Entity:
    return Entity(
        id=row[0],
        name=row[1],
        is_person=row[2],
        id_baggin=row[3],
        id_parent=row[4],
        date_created=_from_iso(row[5]),
        date_updated=_from_iso(row[6]),
        deletion_date=_from_iso(row[7]),
    )


class EntityRepositoryImpl(EntityRepository):
    def __init__(self, database: DatabaseConnectionSqlLite):
        self.database = database

    def insert(self, entity: Entity) -> Entity:
        sql = '''
              INSERT INTO entity
              (name, 
               is_person, 
               id_baggin, 
               id_parent, 
               date_created,
               date_updated,   
               deletion_date)
              VALUES (?, ?, ?, ?, ?, ?, ?) 
              '''

        with self.database.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                sql,
                (
                    entity.name,
                    entity.is_person,
                    entity.id_baggin,
                    entity.id_parent,
                    datetime.now().isoformat(),
                    datetime.now().isoformat(),
                    entity.deletion_date.isoformat() if entity.deletion_date else None,
                )
            )
            _id = cursor.lastrowid
            if cursor.rowcount != 1:
                raise Exception("Erro ao inserir Entity")

            connection.commit()

            if _id:
                entity.id = _id

        return entity

    def update(self, entity: Entity) -> None:
        sql = '''
              UPDATE entity 
              SET name          = ?, 
                  is_person    = ?, 
                  id_baggin          = ?,
                  date_updated      = ?,
                  id_parent   = ?
              WHERE id = ? 
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                entity.name,
                entity.is_person,
                entity.id_baggin,
                datetime.now().isoformat(),
                entity.id_parent,
                entity.id
            ))

            conn.commit()

    def find_by_id(self, entity_id: int) -> Optional[Entity]:
        sql = 'SELECT * FROM entity WHERE id = ?'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (entity_id,))
            row = cursor.fetchone()

            if not row:
                return None

            return _map_row_to_entity(row)

    # 🔹 FIND ALL
    def find_all(self) -> List[Entity]:
        sql = 'SELECT * FROM entity WHERE deletion_date IS NULL'

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            return [_map_row_to_entity(row) for row in rows]


    def delete(self, entity_id: int) -> None:
        sql = '''
              UPDATE entity
              SET deletion_date = ?
              WHERE id = ? \
              '''

        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                datetime.now().isoformat(),
                entity_id
            ))
            conn.commit()

