# api requests

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req) # 200
# print(post_codes_req.headers) # gives the headers
# print(post_codes_req.content) # gives json body as bytes

# Long way
post_codes_dict = json.loads(post_codes_req.content) # turn it into a Python dict
# print(type(post_codes_dict)) # dict

# Short way
print(post_codes_req.json()) # inbuilt method in the requests library to do this

