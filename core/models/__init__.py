"""
Base clases for persistance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.patterns.singleton import Singleton

Base = declarative_base()


class DBManager(metaclass=Singleton):

    def __init__(self, engine, path, echo=False):
        # Create an engine that stores data in the local directory's
        # sqlalchemy_example.db file.
        db_engine = '{}://{}'.format(engine, path)
        self._engine = create_engine(db_engine, echo=echo)

        self._DBSession = sessionmaker()
        self._DBSession.configure(bind=self._engine)

    @property
    def session(self): return self._DBSession

    @property
    def engine(self): return self._engine

    def create(self):
        # Create all tables in the engine. This is equivalent to "Create Table"
        # statements in raw SQL.
        Base.metadata.create_all(self._engine)

    def drop(self):
        Base.metadata.drop_all(self.engine)
