from typing import Annotated

from fastapi import Depends

import models
from services.base import BaseService


class TodoSAService(BaseService):
    def __init__(self, db: models.Db):
        super(TodoSAService, self).__init__(db)

    def get_all(self):
        return self.db.query(models.Todo).all()


def init_todo_service(db: models.Db):
    return TodoSAService(db)


TodoService = Annotated[BaseService, Depends(init_todo_service)]
