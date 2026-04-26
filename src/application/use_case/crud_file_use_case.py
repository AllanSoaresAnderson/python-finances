from typing import Any

from domain.interfaces import CrudFileUseCase, CrudRepository


class CrudFileUseCaseImpl(CrudFileUseCase):
    def __init__(self, repository: CrudRepository):
        self.repository = repository


    def persist(self, entity : Any) -> Any:
        if entity.id is None:
            return self.repository.insert(entity)


        if entity.deletion_date:
            return self.repository.delete(entity.id)

        return self.repository.update(entity)