distance = float(input('Enter trip distance in Km: '))
print(f'Value: {distance * 0.5 if distance <= 200 else distance * 0.45}')
