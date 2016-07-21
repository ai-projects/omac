import datetime
from .base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Enum

repetition_unit_enums = ('hour',
                         'day',
                         'week',
                         'month',
                         'year')

class Task(Base):
    __tablename__ = 'task'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, autoincrement=True, primary_key=True)
    subject = Column(String(80), unique=True, nullable=False)
    notes = Column(String(250))
    reg_date = Column(DateTime, default=datetime.datetime.utcnow())
    deadline = Column(DateTime)
    reminder = Column(DateTime)
    repetition_unit = Column(Enum(repetition_unit_enums)) # FIXME :  AttributeError: 'tuple' object has no attribute 'replace'
    repetition_value = Column(Integer)
