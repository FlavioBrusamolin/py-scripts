name = input('Enter full name: ')

print(name.upper())
print(name.lower())
print(len(name))
print(name.count('a'))

parts = name.split()
parts[-1] = 'do Inatel'
print(' '.join(parts))
