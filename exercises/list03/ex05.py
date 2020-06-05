from ex02 import Employee

class Salesman(Employee):

    _sales_value = float()
    _commission = float()

    def __init__(self, name, address, phone, sector_code, base_salary, tax):
        super().__init__(name, address, phone, sector_code, base_salary, tax)

    @property
    def sales_value(self):
        return self._sales_value

    @sales_value.setter
    def sales_value(self, sales_value):
        self._sales_value = sales_value

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, commission):
        self._commission = commission

    def calculate_salary(self):
        return super().calculate_salary() + self._sales_value * self._commission / 100

if __name__ == "__main__":
    salesman = Salesman(
        input('Name: '),
        input('Address: '),
        input('Phone: '),
        int(input('Sector code: ')),
        float(input('Base salary: ')),
        float(input('Tax (%): '))
    )

    salesman.sales_value = float(input('Sales value: '))
    salesman.commission = float(input('Commission (%): '))

    print(f"Salesman {salesman.name}'s salary: {salesman.calculate_salary()}")