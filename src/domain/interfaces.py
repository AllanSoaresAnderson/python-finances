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

    @abstractmethod
    def find_all(self) -> List[T]:
        """
        Find all entities
        """


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

    @abstractmethod
    def dict_all(self, data: List[Any]) -> List[Dict[str, Any]]:
        """
        Map a list to dicts
        """

    @abstractmethod
    def to_dict(self, data: Any) -> Dict[str, Any]:
        """
        Map a list to dicts
        """


class ShowEntitiesInFileUseCase(ABC):
    @abstractmethod
    def show(self, path: str):
        """
        Show entities in file
        :param path: Path to file
        """


class CsvWriterUseCase(ABC):
    @abstractmethod
    def write(self, path: str, data: List[Dict[str, Any]]):
        """
        Write data to file csv
        :param path: Path to file
        :type path: str
        :param data: List of dicts
        """