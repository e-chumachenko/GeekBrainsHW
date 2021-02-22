from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Clothes(MyAbstractClass):
    def __init__(self, name, color):
        MyAbstractClass.__init__(self, name)
        self.color = color


class Coat(Clothes):
    def __init__(self, name, color, v):
        Clothes.__init__(self, name, color)
        self.v = v

    @property
    def fabric(self):
        return self.v/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, color, h):
        Clothes.__init__(self, name, color)
        self.h = h

    @property
    def fabric(self):
        return 2 * self.h + 0.3


new_coat = Coat('пальто', 'black', 14)
new_costume = Costume('костюм', 'white', 1.7)
print(f'Расход такни на {new_coat.name} - {round(new_coat.fabric, 2)}')
print(f'Расход такни на {new_costume.name} - {round(new_costume.fabric, 2)}')
print(f'Суммарный расход такни - {round((new_coat.fabric + new_costume.fabric), 2)}')
