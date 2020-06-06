numbers = list()

option = 'Y'
while option == 'Y':
    numbers.append(int(input('Enter a number: ')))

    option = input('Keep inserting? Y/N ')

even = list(filter(lambda number: number % 2 == 0, numbers))
odd = list(filter(lambda number: number % 2 != 0, numbers))

print(f'All numbers: {numbers}')
print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')
