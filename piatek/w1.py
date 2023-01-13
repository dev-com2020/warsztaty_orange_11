import logging


def multi(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        # logging.warning('błędna operacja')
        return "błędne dane"
    except ValueError:
        return 0


def multi2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        # logging.warning('błędna operacja')
        return "błędne dane"


def multi3(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        return f"błędne dane - błąd {e.args}"


# print(multi("a", "b"))
# print(multi(3, 3))
# print(multi2("a", "b"))
# print(multi2(3, 3))
# print(multi3("a", "b"))
# print(multi3(3, 3))

valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict = [{}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_dict2 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print(f'Niepoprawne dane: {user}')
        except ValueError:
            print(f'Niepoprawny wiek: {user}')
        else:
            count += 1 if user_age < age else 0
        finally:
            print(f"{i}-{user}")
    return f"Ilość osób spełniających kryteria: {count}"


print(check_age(valid_data, 15))
print(check_age(invalid_dict, 15))
print(check_age(invalid_dict2, 15))
