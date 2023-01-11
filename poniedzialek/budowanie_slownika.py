def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


print(build_person('tomasz', 'kaniecki'))
print(build_person('tomasz', 'kowalski', 33))

