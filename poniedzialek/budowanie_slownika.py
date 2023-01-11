def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name


# while True:
#     print('Podaj imię i nazwisko:')
#     print('Wpisz "q" aby zakończyć')
#     f_name = input("IMIĘ: ")
#     if f_name == 'q':
#         break
#     l_name = input("NAZWISKO: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Witaj {formatted_name}")

# print(build_person('tomasz', 'kaniecki'))
# print(build_person('tomasz', 'kowalski', 33))


