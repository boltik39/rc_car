import configparser
from metaclasses.Singleton import SingletonMetaClass
from pathlib import Path


class ConfigData(metaclass=SingletonMetaClass):
    __READY_CONFIG = None
    __CONFIG_PATH = Path(Path().cwd(), 'settings', 'config.ini')

    def __init__(self):
        self.__ready_data()

    def __ready_data(self):
        self.ready_config = configparser.ConfigParser()
        self.ready_config.read(self.__CONFIG_PATH)

    def get_from_config(self, param):
        return self.ready_config["Config"][param]
