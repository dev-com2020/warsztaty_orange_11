from pprint import pprint

class MySubClass(object):
    pass


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.email!r})')


class Supplier(Contact):
    def order(self, order: "Order"):
        print(f"{order} zamówiono od {self.name}")

c_1 = Contact("Adam", 'tomasz@wp.pl')
c_2 = Contact("Andrzej", 'jakub@wp.pl')
c = Contact("Tomasz", 'tomasz@wp.pl')
s = Supplier("Jakub", 'jakub@wp.pl')
print(c.name, c.email, s.name, s.email)

pprint(c.all_contacts)
s.order('kawa raz!')