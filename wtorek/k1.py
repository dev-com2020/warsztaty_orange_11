import math


class MyFirstClass:
    '''
    Reprezentuje punkty x i y
    '''

    def __init__(self,
                 x=0,
                 y=0
                 ):
        '''
        Inicjalizacja zmiennych klasowych
        :param x: liczba float
        :param y: liczba float
        '''
        self.move(x, y)

    def reset(self):
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


a = MyFirstClass(3, 5)
b = MyFirstClass(0, 5)
print(a.x)

# a.x = 5
# a.y = 4
# b.x = 3
# b.y = 6
a.reset()
b.move(5, 0)
print(b.calculate(a))
assert b.calculate(a) == a.calculate(b)
a.move(3, 4)
print(a.calculate(b))
