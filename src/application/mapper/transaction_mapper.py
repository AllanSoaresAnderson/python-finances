from decimal import Decimal
from typing import Dict, Any, List
from datetime import datetime

from domain.enum import TransactionCategory, FrequencyTransaction, VariableFrequencyTransaction
from domain.interfaces import MapperUseCase
from domain.entities import Transaction

class TransactionMapper(MapperUseCase):

    def map(self, data: Dict[str, str]) -> Any:
        _id = data.get("id")
        frequency = data.get("frequency")
        variable_frequency = data.get("variable_frequency")
        variable_range = data.get("variable_range")
        date_created = data.get("date_created")
        date_updated = data.get("date_updated")
        deletion_date = data.get("deletion_date")
        id_baggin = data.get("id_baggin")
        id_entity = data.get("id_entity")


        return Transaction(
            name=data["name"],
            ident=int(_id) if _id else None,
            category=TransactionCategory[data["category"]],
            start_date=datetime.fromisoformat(data["start_date"]),
            value=Decimal(data["value"]),
            frequency=FrequencyTransaction[frequency] if frequency else None,
            variable_frequency=VariableFrequencyTransaction[variable_frequency] if variable_frequency else None,
            variable_range=int(variable_range) if variable_range else None,
            date_created= datetime.fromisoformat(date_created) if date_created else None,
            date_updated= datetime.fromisoformat(date_updated) if date_updated else None,
            deletion_date= datetime.fromisoformat(deletion_date) if deletion_date else None,
            id_baggin=int(id_baggin) if id_baggin else None,
            id_entity=int(id_entity) if id_entity else None,
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
        return {
            'id': data.id,
            'name': data.name,
            'category': data.category,
            'start_date': data.start_date,
            'value': data.value,
            'frequency': data.frequency,
            'variable_frequency': data.variable_frequency,
            'variable_range': data.variable_range,
            'date_created': data.date_created,
            'date_updated': data.date_updated,
            'deletion_date': data.deletion_date,
            'id_baggin': data.id_baggin,
            'id_entity': data.id_entity
        }