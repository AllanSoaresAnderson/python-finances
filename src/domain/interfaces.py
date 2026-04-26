from abc import ABC, abstractmethod
from typing import List, Dict, Any, TypeVar, Generic
from src.domain.entities import Baggins

T = TypeVar("T")

class CsvReader(ABC):

    @abstractmethod
    def read(self, path: str) -> List[Dict[str, str]]:
        """
        Read a csv file.
        :param path: Path to file
        :type path: str
        :return: List of dicts
        """


class CrudFileUseCase(ABC):
    @abstractmethod
    def persist(self, entity : Any) -> Any:
        """
        Persist an entity into repository
        """

class CrudRepository(ABC, Generic[T]):
    @abstractmethod
    def insert(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, _id: int) -> None:
        pass


class BagginsRepository(CrudRepository[Baggins], ABC):
    pass


class InsertBagginsUseCase(ABC):
    @abstractmethod
    def insert(self, baggins: Baggins) -> Baggins:
        """
        Insert a baggins into repository
        :param baggins: Baggins
        :type baggins: Baggins
        :return: Baggins
        """


class RegisterFileUseCase(ABC):

    @abstractmethod
    def register(self, path: str):
        """
        Register a file
        """


class MapperUseCase(ABC):
    @abstractmethod
    def map(self, data: Dict[str, str]) -> Any:
        """
        Map a dict to an entity
        """

    @abstractmethod
    def map_all(self, data: List[Dict[str, str]]) -> List[Any]:
        """
        Map a list of dicts to entities
        """

