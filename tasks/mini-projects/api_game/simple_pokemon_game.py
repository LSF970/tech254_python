# This Program uses a simple system to declare a winner. Look to advance on this.

import requests
import json
import random

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

# Select CPU pokemon
cpu = random.choice(pokemon_list)
cpu_name = cpu['name']
print(cpu_name)

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# get cpu data from API
cpu_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(cpu_name)
cpu_response = requests.get(cpu_url)
cpu_data = json.loads(cpu_response.text)


# to get abilities
ability1 = pokemon_data['abilities'][0]
ability2 = pokemon_data['abilities'][1]
pokemon_ability1 = ability1['ability']
pokemon_ability2 = ability2['ability']

# to get base experience
base_xp = int(pokemon_data['base_experience'])
cpu_base_xp = int(cpu_data['base_experience'])



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


print(base_xp)
print(cpu_base_xp)
if base_xp > cpu_base_xp:
    print("Hooray! Your pokemon defeated the oppenent's " + cpu_name.capitalize())
elif cpu_base_xp > base_xp:
    print("Oh no! Your pokemon has been defeated by your opponent's " + cpu_name.capitalize())
else:
    print("Wow! Both your pokemon and the oppenent's " + cpu_name.capitalize() + " Have fainted at the same time! It is a draw!")



