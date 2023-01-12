import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, moje ID to {self.id}")


# people = [
#     Person("Jacek", "Kowalski", 1),
#     Person("Mateusz", "Jaworski", 2)
# ]
# with open('data.pickle', 'wb') as stream:
#     pickle.dump(people, stream)
