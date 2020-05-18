numbers = list()

for i in range(6):
    value = int(input('Enter a number: '))
    numbers.append(value)

result = sum(list(filter(lambda number: number % 2 != 0, numbers)))
print(f'Result: {result}')
