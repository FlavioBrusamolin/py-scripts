limit = 80
velocity = float(input('Enter car velocity: '))

if velocity <= limit:
    print('Good trip!')
else:
    print('You received a traffic ticket')
    print(f'Value: {(velocity - limit) * 50} reais')
