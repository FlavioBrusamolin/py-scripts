from ex01 import Person


class Employee(Person):

    def __init__(self, name, address, phone, sector_code, base_salary, tax):
        super().__init__(name, address, phone)
        self.__sector_code = sector_code
        self.__base_salary = base_salary
        self.__tax = tax

    @property
    def sector_code(self):
        return self.__sector_code

    @sector_code.setter
    def sector_code(self, sector_code):
        self.__sector_code = sector_code

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, base_salary):
        self.__base_salary = base_salary

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, tax):
        self.__tax = tax

    def calculate_salary(self):
        return self.__base_salary * (1 - self.__tax / 100)


if __name__ == "__main__":
    employee = Employee(
        input('Name: '),
        input('Address: '),
        input('Phone: '),
        int(input('Sector code: ')),
        float(input('Base salary: ')),
        float(input('Tax (%): '))
    )

    print(f"Employee {employee.name}'s salary: {employee.calculate_salary()}")
