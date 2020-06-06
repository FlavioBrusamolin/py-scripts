from statistics import mean

people = list()

option = 'Y'
while option == 'Y':
    people.append({
        'name': input(f'Enter the name of person: '),
        'gender': input(f'Enter the gender (Male or Female) of person: '),
        'age': int(input(f'Enter the age of person: '))
    })

    option = input('Keep inserting? Y/N ')

print(f'Amount of people: {len(people)}')

average_age = mean(list(map(lambda person: person['age'], people)))
print(f'Average age: {average_age}')

women = list(filter(lambda person: person['gender'] == 'Female', people))
print(f'Women: {women}')

older = list(filter(lambda person: person['age'] > average_age, people))
print(f'Older: {older}')
