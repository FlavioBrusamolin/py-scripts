numbers = list()

option = 'Y'
while option == 'Y':
    numbers.append(float(input('Enter a number: ')))

    option = input('Keep inserting? Y/N ')

print(f'Amount of numbers entered: {len(numbers)}')

numbers.sort(reverse=True)
print(f'Ordered list: {numbers}')

print(f"Number 5 {'is' if 5 in numbers else 'is not'} in the list")
