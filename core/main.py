import configparser
import os

from core.managers import TaskManager
from core.models import DBManager

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class ConfigureParser(object):

    def __init__(self, configuration_path):

        self._config = configparser.ConfigParser()
        config_path = os.path.join(BASE_DIR, configuration_path)
        self._config.read(config_path)

    @property
    def persistence(self):
        return self._config.get('persistence', 'engine')

    @property
    def persistence_path(self):
        return self._config.get('persistence', 'path')

    @property
    def logger(self):
        return self._config.get('logger', 'path')


class Engine:

    def __init__(self, configuration, reset_database=False, echo_database=False, before_start=None, after_start=None):

        self._configuration = ConfigureParser(configuration)
        self._persistence = DBManager(self._configuration.persistence,
                                      self._configuration.persistence_path,
                                      echo=echo_database)
        self._logger = None

        self._task_manager = TaskManager(self)

        if reset_database:
            self.reset_database()

    @property
    def persistence(self):
        return self._persistence

    @property
    def logger(self):
        return self._logger

    @property
    def task_manager(self):
        return self._task_manager

    def reset_database(self):
        self._persistence.drop()
        self._persistence.create()
