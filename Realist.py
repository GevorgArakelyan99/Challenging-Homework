from Barev_class import Barev


class Realist(Barev):
    def __init__(self, name: str):
        super().__init__(name)
        self.sub = None

    def __sub__(self, other):
        self.sub = self.get_age() - other.get_age()
        return self.sub

    def process(self, other):
        if self.sub is True:
            return f'Ողջույն {other.name}'
        else:
            return f'Բարև {other.name}'
