def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def glowna():
    def wew(a, b):
        return a * b

    x = wew(5, 5)
    return x


def f():
    def fWew(a, b):
        return a * b

    return fWew

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()
    return wew

@dekor
def hej():
    print("Hej!")

hej()

x = f()
# print(x(3, 3))
# print(glowna())


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b
#
#
# print(wykonaj(dodaj, 2, 3))
# print(wykonaj(odejmij, 4, 3))
