from configparser import ConfigParser


class Divulgation:
    def __init__(self, filename):
        self.filename = filename
        self.reload()

    def reload(self):
        self.file = ConfigParser()
        self.file.read(self.filename, encoding='utf-8')

    def get_message(self, key, default=None):
        return self.file.get('message', key, fallback=default)
