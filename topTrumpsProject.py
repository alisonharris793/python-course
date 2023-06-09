# MoSCoW
#
# Must Have (non-negotiable product needs that are mandatory for the team)
# Generate a random number between 1 and 151 to use as the Pokemon ID number
# Using the Pokemon API get a Pokemon based on its ID number
# Create a dictionary that contains the returned Pokemon's name, id, height and weight (★ https://pokeapi.co/)
# Get a random Pokemon for the player and another for their opponent
# Ask the user which stat they want to use (id, height or weight)
# Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
#
# Should Have (important initiatives that are not vital, but add significant value)
# Get multiple random Pokemon and let the player decide which stat that they want to use
# Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game
# Record high scores for players and store them in a file
#
# Could Have (nice to have initiatives that will have a small impact if left out)
# Introducing the game to the player and asking if they'd like to play
# Ask if the player would like to play again
# Allow the opponent (computer) to choose a stat that they would like to compare
#
# Will Not Have (initiatives that are not priority for this specific time frame)
# Changing API option
# Using different stats for the Pokemon from the API

import random
import requests


#EXTENTION welcome player to the game
print("Welcome to the Pokemon Top Trumps Game!\n")
playername = input("Please enter your name: ")
print("Hello " + playername + ", get ready to enter the world of Pokemon!\n")
computer = "Computer"
print("You are playing against " + computer +  ", get ready...\n")


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

random_pokemon()


# this is a function that runs the game three times and keeps a hold of the overall score
def run():
    score = 0
    for x in range(3):
        my_pokemon = random_pokemon()
        print('you were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        outcome = compare_stats(my_pokemon[stat_choice], opponent_pokemon[stat_choice])
        if outcome == True:
            score += 1
    calculate_win(score)

#def run():
#    player_score = 0
#    opponent_score = 0

#        pokemon_1 = random_pokemon()
#        pokemon_2 = random_pokemon()
#        pokemon_3 = random_pokemon()

#        print("\nPokemon 1 - {} - id: {}    weight: {}    height: {}".format(pokemon_1["name"], pokemon_1["id"], pokemon_1["weight"], pokemon_1["height"]))
#        print("Pokemon 2 - {} - id: {}    weight: {}    height: {}".format(pokemon_2["name"], pokemon_2["id"], pokemon_2["weight"], pokemon_2["height"]))
#        print("Pokemon 3 - {} - id: {}    weight: {}    height: {}\n".format(pokemon_3["name"], pokemon_3["id"], pokemon_3["weight"], pokemon_3["height"]))

#    player_choice = input("\n{} choose a pokemon to battle - {}, {} or {} : \n".format(playername, pokemon_1["name"], pokemon_2["name"], pokemon_3["name"]))

#    if player_choice == pokemon_1["name"]:
#       player_pokemon = pokemon_1
#        print("\n{} has chosen to battle {}.".format(playername, pokemon_1))
#    elif player_choice == pokemon_2["name"]:
#        player_pokemon = pokemon_2
#        print("\n{} has chosen to battle {}.".format(playername, pokemon_2))
#    elif player_choice == pokemon_3["name"]:
#        player_pokemon = pokemon_3
#        print("\n{} has chosen to battle {}.".format(playername, pokemon_3))

#   stat_choice = input("\n{} which stat do you want to use? (id, height, weight)".format(playername))

#   opponent_pokemon = random_pokemon()
#    print('\nThe computer chose {}'.format(opponent_pokemon['name']))

#   player_stat = player_pokemon[stat_choice]
#   opponent_stat = opponent_pokemon[stat-choice]
#
#    if player_stat > opponent_stat:
#       print("\n{}\'s {} was {} and the computers was {} ~~~ YOU WIN!".format(playername, stat_choice, player_stat, opponnt_stat))
#
#        player_score = player_score + 1
#
#    elif player_stat < opponent_stat:
#        print("\n{}\' {} was {} and the computers was {} ~~~ YOU LOSE!".format(playername, stat_choice, player_stat, opponent_stat))
#
#        opponent_score = opponent_score + 1
#
#    else:
#        print("\n~~~DRAW~~~")
#
#        print("\nAfter that round {}\'s score is: {} \nComputers score is: {}\n".format(playername, player_score, opponent_score))


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

#extention - ask if the player would like to play again
def play_again():
    play_again = input("Would you like to play again " +playername+ "? yes/no ")
    print("\n")
    if play_again == "yes":
        print("\n~~~~NEW~~~~ROUND~~~~")

    elif play_again == "no":
        print("\n~~~~GAME~~~~OVER~~~~")

run()
play_again()
#my issue with this part of the code is that it will play again despite the player saying no, in attempts to fix this i have taken away the run(), however
# this led to the code asking the player if they want to play again after entering their name, and resulted in the game not starting




