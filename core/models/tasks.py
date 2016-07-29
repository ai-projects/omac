import datetime
import enum

from core.models import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Enum


class Task(Base):
    __tablename__ = 'task'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, autoincrement=True, primary_key=True)
    subject = Column(String(80), unique=True, nullable=False)
    notes = Column(String(250))
    reg_date = Column(DateTime, default=datetime.datetime.utcnow())
    deadline = Column(DateTime)
    exec_date = Column(DateTime)
    reminder = Column(DateTime)
    repetition_unit = Column(Enum('day',
                                  'month',
                                  'week',
                                  'year',
                                  'repetition_types'))

    # FIXME :  AttributeError: 'tuple' object has no attribute 'replace'
    repetition_value = Column(Integer)

    def __repr__(self):
        return "<Task object id[{id}] (" \
               "subject='{subject}', notes='{notes}', reg_date='{reg_date}', " \
               "deadline='{deadline}', reminder='{reminder}', " \
               "repetition_unit='{repetition_unit}', repetition_value='{repetition_value}" \
               ")'".format(**self.__dict__)
