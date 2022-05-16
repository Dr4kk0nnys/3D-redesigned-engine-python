from distutils.command.config import config
import enum
import json


class Configurations:

    def __init__(self) -> None:
        self.read_configurations()

    def read_configurations(self):
        with open('./configs.json', 'r') as file:
            self.configs = json.load(file)
            file.close()

        """ Note: More customizable configs """
        self.configs['half_width'] = self.configs['width'] // 2
        self.configs['half_height'] = self.configs['height'] // 2


if __name__ == '__main__':
    configurations = Configurations()
