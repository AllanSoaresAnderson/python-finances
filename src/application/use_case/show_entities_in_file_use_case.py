from domain.interfaces import ShowEntitiesInFileUseCase, CrudRepository, MapperUseCase, CsvWriterUseCase


class ShowEntitiesInFileUseCaseImpl(ShowEntitiesInFileUseCase):

    def __init__(
            self,
            repository: CrudRepository,
            mapper: MapperUseCase,
            writer: CsvWriterUseCase
    ):
        self.repository = repository
        self.mapper = mapper
        self.writer = writer


    def show(self, path: str):
        entities = self.repository.find_all()
        dict_entities = self.mapper.dict_all(entities)
        self.writer.write(path, dict_entities)



