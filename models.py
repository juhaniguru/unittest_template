# coding: utf-8
import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

Base = declarative_base()
metadata = Base.metadata

load_dotenv()

engine = create_engine(os.getenv('DB'))
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)

    def __eq__(self, other):
        return isinstance(other, Todo) and other.id == self.id and other.title == self.title


def init_db():
    try:
        db = session()
        yield db
    finally:
        db.close()


Db = Annotated[Session, Depends(init_db)]


