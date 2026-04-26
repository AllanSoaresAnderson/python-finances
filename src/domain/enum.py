from enum import Enum


class TransactionCategory(Enum):
    FIXED = 'F'
    EVENTUAL = 'E'


class FrequencyTransaction (Enum):
    DAILY = 'D'
    WEEKLY = 'W'
    MONTHLY = 'M'
    ANNUALLY = 'A'
    VARIABLE = 'V'


class VariableFrequencyTransaction(Enum):
    MONTH = 'M'
    YEAR = 'Y'
    WEEK = 'W'
    DAY = 'D'


class TypeBaggins(Enum):
    MONTHLY = 'M'
    VARIABLE = 'V'
