import csv
from typing import List, Dict

from domain.interfaces import CsvReader


class CsvReaderImpl(CsvReader):

    def read(self, path: str) -> List[Dict[str, str]]:
        data = []

        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                data.append(row)

        return data