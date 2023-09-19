# This Program gets the dat for a user entered Pokemon AND a randomly generated CPU Pokemon.

import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

# Ask the user to choose a pokemon
print('Enter your pokemon:')
# for pokemon in pokemon_list:
    # print(pokemon['name'])

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get abilities
ability1 = pokemon_data['abilities'][0]
ability2 = pokemon_data['abilities'][1]
pokemon_ability1 = ability1['ability']
pokemon_ability2 = ability2['ability']

# to get base experience
base_xp = int(pokemon_data['base_experience'])



# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Get the pokemon's stats
hp = pokemon_data['stats'][0]
hp_int = hp['base_stat']

attack = pokemon_data['stats'][1]
attack_int = attack['base_stat']

defense = pokemon_data['stats'][2]
defense_int = attack['base_stat']

sp_attack = pokemon_data['stats'][3]
sp_attack_int = attack['base_stat']

sp_defense = pokemon_data['stats'][4]
sp_defense_int = attack['base_stat']

speed = pokemon_data['stats'][5]
speed_int = attack['base_stat']






# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']).capitalize())
print('HP: {}' .format(hp_int))
print('Attack: {}' .format(attack_int))
print('Special Attack: {}' .format(sp_attack_int))
print('Defense: {}' .format(defense_int))
print('Special Defense: {}' .format(sp_defense_int))
print('Speed: {}' .format(speed_int))
# print('Weight: {}'.format(weight_formatted) + "(kgs)")
# print('Height: {}'.format(height_formatted) + "(m)")
print('Ability 1: {}'.format(pokemon_ability1['name'].capitalize()))
print('Ability 2: {}'.format(pokemon_ability2['name'].capitalize()))