import unittest

from fastapi.testclient import TestClient

import main
import models


class TestsTodosController(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        models.metadata.create_all(bind=models.engine)
        cls.client = TestClient(main.app)

    @classmethod
    def tearDownClass(cls) -> None:
        models.metadata.drop_all(bind=models.engine)

    def test_get_all_todos(self):
        res = self.client.get('/api/todos/')
        self.assertEqual(res.status_code, 200)
