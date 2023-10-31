import unittest

import models
from services.base import BaseService
from services.todos_sa import TodoService, init_todo_service


class TodoSAServiceMockEmpty(BaseService):
    def __init__(self, db: models.Db):
        super(TodoSAServiceMockEmpty, self).__init__(db)

    def get_all(self):
        return []


class TodoSAServiceMock(BaseService):
    def __init__(self, db: models.Db):
        super(TodoSAServiceMock, self).__init__(db)

    def get_all(self):
        return [models.Todo(id=1, title='titteli', body='body')]


class TestsTodosServiceMock(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_empty = TodoSAServiceMockEmpty(None)
        self.mock = TodoSAServiceMock(None)

    def test_get_all_empty(self):
        res = self.mock_empty.get_all()
        self.assertEqual(res, [])

    def test_get_all_not_empty(self):
        todos = self.mock.get_all()
        compare = models.Todo(id=1, title='titteli', body='body')

        self.assertEqual(todos[0], compare)
