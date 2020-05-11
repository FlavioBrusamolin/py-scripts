weights = list()

for i in range(5):
    value = float(input('Enter weight: '))
    weights.append(value)

print(f'Highest: {max(weights)}')
print(f'Lowest: {min(weights)}')
