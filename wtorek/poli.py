class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print(self.__predkosc)

    def __zmien_bieg(self):
        print("Zmiana biegu!")


c1 = Car('bmw', 2014)
c1.gaz()
c1.gaz()
c1.gaz()
c1.gaz()
c1.licznik()
c1.hamuj()
c1.hamuj()
c1.hamuj()
c1.hamuj()
c1.licznik()

