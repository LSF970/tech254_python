import json
import os

# json.load() --> takes a file object and returns the json object inside. used to read encoded json data from a file and convert it into a Python dict automatically.

# json.loads() --> takes a valid json string and parses it into a valid Python dictionary

# So load takes a file path whereas loads takes  file contents as a string.

# Load for JSON files
# Loads for raw JSON

# Use read() to deserialise a json file using loads


json = json.loads(open("C:/Users/Luke/Documents/tech_254/python/scripting/example_json.json").read())
value = json["name"]
print(value)

for key in json: 
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))