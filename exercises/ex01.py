value = input('Enter a value: ')

if value.isnumeric():
    print('Formed by numbers')
elif value.isalpha():
    print('Formed by leters')
elif value.isalnum():
    print('Formed by alphanumerics')
else:
    print('Unidentified type')
