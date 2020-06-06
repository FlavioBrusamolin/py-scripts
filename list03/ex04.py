from ex02 import Employee


class Operator(Employee):

    __production_value = float()
    __commission = float()

    def __init__(self, name, address, phone, sector_code, base_salary, tax):
        super().__init__(name, address, phone, sector_code, base_salary, tax)

    @property
    def production_value(self):
        return self.__production_value

    @production_value.setter
    def production_value(self, production_value):
        self.__production_value = production_value

    @property
    def commission(self):
        return self.__commission

    @commission.setter
    def commission(self, commission):
        self.__commission = commission

    def calculate_salary(self):
        return super().calculate_salary() + self.__production_value * self.__commission / 100


if __name__ == "__main__":
    operator = Operator(
        input('Name: '),
        input('Address: '),
        input('Phone: '),
        int(input('Sector code: ')),
        float(input('Base salary: ')),
        float(input('Tax (%): '))
    )

    operator.production_value = float(input('Production value: '))
    operator.commission = float(input('Commission (%): '))

    print(f"Operator {operator.name}'s salary: {operator.calculate_salary()}")
