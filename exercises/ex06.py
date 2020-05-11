number = int(input('Enter a number between 0 and 9999: '))

r_thousands = (number % 1000)
r_hundreds = (r_thousands % 100)
r_dozens = (r_hundreds % 10)

print(f'Thousands: {int(number / 1000)}')
print(f'Hundreds: {int(r_thousands / 100)}')
print(f'Dozens: {int(r_hundreds / 10)}')
print(f'Units: {r_dozens}')
