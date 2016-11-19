import unittest
from sqlite3 import IntegrityError

from core.main import Engine
from core.models.tasks import Task


class TestUM(unittest.TestCase):
    def setUp(self):
        # TODO : create test setup
        self.engine = Engine('omac.conf', reset_database=True, echo_database=False)

    def test_task_unique_subject(self):
        # TODO : test unique subject of telepot
        task_manager = self.engine.task_manager
        task_manager.create_task(subject='Create tests')
        with self.assertRaises(IntegrityError):
            task = Task(subject='Create tests')
            task_manager.add_task(task)

