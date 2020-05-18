name = input("Enter player's name: ")
number_of_matches = int(input("Enter number of player's matches: "))

goals_per_match = dict()
for i in range(number_of_matches):
    goals_per_match[f'match{i + 1}'] = int(
        input(f'Enter amount of goals scored by player in match {i + 1}: '))

total_goals = sum(goals_per_match.values())

player = {
    'name': name,
    'number_of_matches': number_of_matches,
    'goals_per_match': goals_per_match,
    'total_goals': total_goals
}

print(f'Player statistics: {player}')
