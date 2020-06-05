class Person:

    def __init__(self, name, address, phone):
        self._name = name
        self._address = address
        self._phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    def introduce_yourself(self):
        return {
            'name': self._name,
            'address': self._address,
            'phone': self._phone
        }

    def exchange_phone(self, other):
        self._phone, other.phone = other.phone, self._phone

if __name__ == "__main__":
    p1 = Person(
        input('P1 Name: '),
        input('P1 Address: '),
        input('P1 Phone: ')
    )

    p2 = Person(
        input('P2 Name: '),
        input('P2 Address: '),
        input('P2 Phone: ')
    )

    print(f'P1 personal data: {p1.introduce_yourself()}')
    print(f'P2 personal data: {p2.introduce_yourself()}')

    p1.exchange_phone(p2)
    print(f'P1 new phone: {p1.phone}')
    print(f'P2 new phone: {p2.phone}')