def convert(value, unit):
    switcher = {
        'cm': value * 100.0,
        'mm': value * 1000.0
    }

    print(f"{unit}: {switcher.get(unit, 'Enter unit in cm or mm')}")


value = float(input('Enter a value in meters: '))
convert(value, 'cm')
convert(value, 'mm')
