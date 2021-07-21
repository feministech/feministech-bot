from random import choice


class RandomList:
    def __init__(self, filename):
        self.filename = filename
        self.reload()

    def reload(self):
        with open(self.filename, encoding='utf-8') as fp:
            self.list = (line.strip() for line in fp.readlines())
            self.list = [line for line in self.list if line]

    def get_random(self):
        return choice(self.list)
