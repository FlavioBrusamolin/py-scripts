class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    def introduce_yourself(self):
        return {
            'name': self.__name,
            'address': self.__address,
            'phone': self.__phone
        }

    def exchange_phone(self, other):
        self.__phone, other.phone = other.phone, self.__phone


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
