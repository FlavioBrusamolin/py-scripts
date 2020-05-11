numbers = list()

for i in range(3):
    value = float(input('Enter a number: '))
    numbers.append(value)

print(f'Highest: {max(numbers)}')
print(f'Smallest: {min(numbers)}')
