def apply_discount(price, discount):
    return price - ((price * discount) / 100.0)


price = float(input('Enter price: '))
discount = int(input('Enter discount: '))

print(f'New price: {apply_discount(price, discount)}')
