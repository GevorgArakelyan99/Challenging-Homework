from Barev_class import Barev


class Pozitiv(Barev):
    def __init__(self, name: str):
        super().__init__(name)

    def process(self, other):
        return f'Ողջույն {other.name}'
