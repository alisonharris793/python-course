import random
import requests

# this is a function that calls the pokemon API and returns four stats from a random pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
    }

# this is a function that runs the game three times and keeps a hold of the overall score
def run():
    score = 0
    for x in range(3):
        my_pokemon = random_pokemon()
        print('You were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        outcome = compare_stats(my_pokemon[stat_choice], opponent_pokemon[stat_choice])
        if outcome == True:
            score += 1
    calculate_win(score)

# this is a function to calculate whether my score is enough to win overall
def calculate_win(score):
    if score >= 2:
        print('You are the overall winner!')
    else:
        print('You have lost!')


# this is a function to compare the stats of both pokemon
# this will return true or false depending on the outcome of the compare_stats
def compare_stats(my_stat, opponent_stat):
    if my_stat > opponent_stat:
        print('You Win This Round!')
        return True
    elif my_stat < opponent_stat:
        print('You Lose This Round!')
        return False
    else:
        print('Draw On This Round!')
        return False


run()
