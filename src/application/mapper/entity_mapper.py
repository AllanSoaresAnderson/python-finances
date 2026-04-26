from dataclasses import asdict
from typing import Dict, Any, List
from datetime import datetime

from domain.interfaces import MapperUseCase
from domain.entities import Entity

class EntityMapper(MapperUseCase):

    def map(self, data: Dict[str, str]) -> Any:
        _id = data.get("id")
        is_person = data.get("is_person")
        id_baggin = data.get("id_baggin")

        id_parent = data.get("id_parent")
        date_created = data.get("date_created")
        date_updated = data.get("date_updated")
        deletion_date = data.get("deletion_date")


        return Entity(
            name=data["name"],
            id=int(_id) if _id else None,
            is_person=True if is_person else False,
            id_baggin=int(id_baggin) if id_baggin else None,
            id_parent=int(id_parent) if id_parent else None,
            date_created= datetime.fromisoformat(date_created) if date_created else None,
            date_updated= datetime.fromisoformat(date_updated) if date_updated else None,
            deletion_date= datetime.fromisoformat(deletion_date) if deletion_date else None,
        )

    def map_all(self, data: List[Dict[str, str]]) -> List[Any]:
        result = []
        for d in data:
            result.append(self.map(d))
        return result

    def dict_all(self, data: List[Any]) -> List[Dict[str, Any]]:
        result = []
        for d in data:
            result.append(self.to_dict(d))
        return result

    def to_dict(self, data: Any) -> Dict[str, Any]:
        return asdict(data)