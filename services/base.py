import models


class BaseService:
    def __init__(self, db: models.Db):
        self.db = db

    def get_all(self):
        pass
