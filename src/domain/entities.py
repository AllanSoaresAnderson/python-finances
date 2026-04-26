from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

from src.domain.enum import TransactionCategory, FrequencyTransaction, VariableFrequencyTransaction, TypeBaggins


@dataclass
class Baggins:
    id: Optional[int]
    name: str
    start_date: Optional[datetime]
    type: TypeBaggins = TypeBaggins.MONTHLY
    amount_time: Optional[int] = None
    date_created: Optional[datetime] = None
    deletion_date: Optional[datetime] = None


@dataclass
class Entity:
    id: int
    name: str
    is_person: bool
    id_baggin: int

    id_parent: Optional[int] = None
    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    deletion_date: Optional[datetime] = None


@dataclass
class Installment:
    id: int
    name: str
    value: Decimal
    id_transaction: Optional[int] = None

class Transaction:

    def __init__(
            self,
            name: str,
            category: TransactionCategory,
            start_date: datetime,
            value: Decimal,
            ident: int = None,
            frequency: FrequencyTransaction = None,
            variable_frequency: VariableFrequencyTransaction = None,
            variable_range: int = None,
            date_created: datetime = None,
            date_updated: datetime = None,
            deletion_date: datetime = None,
            id_baggin: int = None,
            id_entity: int = None,
    ):
        self.name = name
        self.category = category
        self.start_date = start_date
        self.value = value
        self.id = ident
        self.frequency = frequency
        self.variable_frequency = variable_frequency
        self.variable_range = variable_range
        self.date_created = date_created
        self.date_updated = date_updated
        self.deletion_date = deletion_date
        self.id_baggin = id_baggin
        self.id_entity = id_entity


    def is_earning(self):
        return self.value >= Decimal(0)


class Payment:

    def __init__(
            self,
            name: str,
            value: Decimal,
            reference_date: datetime,
            id_baggin: int,
            id_transaction: int = None,
            id_installment: int = None,
            identifier: int = None,
    ):
        self.name = name
        self.value = value
        self.reference_date = reference_date
        self.id_baggin = id_baggin
        self.id_transaction = id_transaction
        self.id_installment = id_installment
        self.id = identifier


    def is_expense(self):
        return self.value < Decimal(0)

    def is_earning(self):
        return not self.is_expense()











