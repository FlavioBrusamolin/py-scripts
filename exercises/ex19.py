from statistics import mean

people = list()

for i in range(4):
    name = input(f'Enter the name of person {i + 1}: ')
    age = int(input(f'Enter the age of person {i + 1}: '))
    gender = input(f'Enter the gender (Male or Female) of person {i + 1}: ')

    people.append({
        'name': name,
        'age': age,
        'gender': gender
    })

people.sort(key=lambda person: person['age'], reverse=True)

ages = list(map(lambda person: person['age'], people))
print(f'Average age: {mean(ages)}')

men = list(filter(lambda person: person['gender'] == 'Male', people))
print(f"Older man: {men[0]['name']}")

younger_women = list(filter(
    lambda person: person['gender'] == 'Female' and person['age'] < 20, people))
print(f'Number of women under 20: {len(younger_women)}')
