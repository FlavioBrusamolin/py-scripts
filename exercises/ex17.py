from datetime import date

years = list()

for i in range(7):
    value = int(input('Enter year of birth: '))
    years.append(value)

ages = list(map(lambda year: date.today().year - year, years))
olders = list(filter(lambda age: age >= 18, ages))

print(f'Number of adults: {len(olders)}')
