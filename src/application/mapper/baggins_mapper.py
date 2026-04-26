from dataclasses import asdict
from typing import Dict, Any, List
from datetime import datetime

from domain.enum import TypeBaggins
from domain.interfaces import MapperUseCase
from domain.entities import Baggins

class BagginsMapper(MapperUseCase):

    def map(self, data: Dict[str, str]) -> Any:
        _id = data.get("id")
        start_date = data.get("start_date")
        _type = data.get("type")
        amount_time = data.get("amount_time")
        date_created = data.get("date_created")
        deletion_date = data.get("deletion_date")
        return Baggins(
            name=data["name"],
            id=int(_id) if _id else None,
            start_date= datetime.fromisoformat(start_date) if start_date else None,
            type=TypeBaggins[_type] if _type else TypeBaggins.MONTHLY,
            amount_time= int(amount_time) if amount_time else None,
            date_created= datetime.fromisoformat(date_created) if date_created else None,
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