from domain.interfaces import RegisterFileUseCase, CsvReader, MapperUseCase, CrudFileUseCase


class RegisterFileUseCaseImpl(RegisterFileUseCase):
    def __init__(
            self,
            reader: CsvReader,
            mapper: MapperUseCase,
            repository: CrudFileUseCase
    ):
        self.reader = reader
        self.mapper = mapper
        self.repository = repository

    def register(self, path: str):
        data = self.reader.read(path)
        entities = self.mapper.map_all(data)
        for entity in entities:
            self.repository.persist(entity)

