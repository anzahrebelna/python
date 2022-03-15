from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, parametrs):
        self.paramerts = parametrs

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.paramerts / 6.5) + 0.5

class Costume(Clothes):

    @property
    def consumption(self):
        return 2 * self.paramerts + 0.3

coat = Coat(46)
costume = Costume(164)

print(coat + costume)
