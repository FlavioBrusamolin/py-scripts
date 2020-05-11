num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

switcher = {
    1: num1 + num2,
    2: num1 * num2,
    3: num1 if num1 > num2 else num2,
    4: 'Bye'
}

option = 0

while option != 4:
    option = int(
        input('1 - Sum \n2 - Multiply \n3 - Biggest number \n4 - Exit \n'))

    print(f"Result: {switcher.get(option, 'Invalid option')}")
