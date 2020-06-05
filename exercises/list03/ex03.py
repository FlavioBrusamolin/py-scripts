from ex02 import Employee

class Administrator(Employee):

    _financial_help = float()

    def __init__(self, name, address, phone, sector_code, base_salary, tax):
        super().__init__(name, address, phone, sector_code, base_salary, tax)

    @property
    def financial_help(self):
        return self._financial_help

    @financial_help.setter
    def financial_help(self, financial_help):
        self._financial_help = financial_help

    def calculate_salary(self):
        return super().calculate_salary() + self._financial_help

if __name__ == "__main__":
    admin = Administrator(
        input('Name: '),
        input('Address: '),
        input('Phone: '),
        int(input('Sector code: ')),
        float(input('Base salary: ')),
        float(input('Tax (%): '))
    )

    admin.financial_help = float(input('Financial help: '))

    print(f"Administrator {admin.name}'s salary: {admin.calculate_salary()}")