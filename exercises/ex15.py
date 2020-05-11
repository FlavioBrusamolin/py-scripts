price = float(input('Enter product value: '))
option = int(input(
    'Enter your payment option: \n0 - Cash payment \n1 - Debit card \n2 - Credit card \n'))

switcher = {
    0: price - (price * 0.1),
    1: price - (price * 0.05),
    2: price + (price * 0.15)
}

print(f"New price: {switcher.get(option, 'Invalid option')}")
