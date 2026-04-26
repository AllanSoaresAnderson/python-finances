from typing import List, Dict, Any
from csv import DictWriter
from domain.interfaces import CsvWriterUseCase


class CsvWriterUseCaseImpl(CsvWriterUseCase):

    def write(self, path: str, data: List[Dict[str, Any]]):
        if not data:
            return

        def normalize(value):
            from datetime import datetime
            from enum import Enum
            from decimal import Decimal

            if isinstance(value, datetime):
                return value.isoformat()
            if isinstance(value, Enum):
                return value.name
            if isinstance(value, Decimal):
                return str(value)
            return value

        normalized_data = [
            {k: normalize(v) for k, v in row.items()}
            for row in data
        ]

        fieldnames = list(normalized_data[0].keys())

        with open(path, mode='w', newline='', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(normalized_data)