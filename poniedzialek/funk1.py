def powitanie(imie: str):
    print(f"Witaj, {imie.title()} !")


def powitanie2(imie: str, wiek=18, *liczba):
    '''Funkcja zwraca łańcuch znaków z parametrami'''
    return f"Witaj, {imie.title()}, masz {wiek} lat. A magiczna liczba to {liczba} !"


powitanie("tomek")
powitanie(str(456))
print(powitanie2("jarek"))
imie = powitanie2("jarek", 25, 5, 55, 22, 11, 33)

imiona = []
imiona.append(imie)
print(imiona)
