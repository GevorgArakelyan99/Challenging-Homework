import random


class Barev:
    def __init__(self, name: str):
        self.name = name
        self.age = random.randint(20, 40)


    def get_age(self):
        return self.age
