from datetime import date

year_of_birth = int(input('Enter your year of birth: '))
age = date.today().year - year_of_birth

if age <= 9:
    print('MIRIM')
elif age <= 14:
    print('INFANTIL')
elif age <= 19:
    print('JÚNIOR')
elif age <= 20:
    print('SENIOR')
else:
    print('MASTER')
