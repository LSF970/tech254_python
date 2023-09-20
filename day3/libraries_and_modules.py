# Libraries and Modules

# Python has very extensive libraries and modules, this is great for us as DevOps engineers!

# Module = Single file of functions, classes, variables etc. That you can bring in and use in another Python file.

# Library = Collection of modules. Needs to be installed with pip.

import math
import random
import requests

# num_float = 23.01
#
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)

# rand_list = [1, 2, 3, 4, 5, 6, 7]
# print(random.choice(rand_list))
#
# rand_num = random.randint(1, 10)

request_poke = requests.get("https://pokeapi.co/api/v2/pokemon/krokorok")

print(request_poke.status_code)
print(request_poke.content)

bbc_content = request_poke.content


