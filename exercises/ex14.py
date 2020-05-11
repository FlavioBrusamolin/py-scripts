weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

imc = weight / (height * height)

if imc < 18.5:
    print('Under weight')
elif imc < 25:
    print('Ideal weight')
elif imc < 30:
    print('Overweight')
elif imc < 40:
    print('Obesity')
else:
    print('Morbid obesity')
