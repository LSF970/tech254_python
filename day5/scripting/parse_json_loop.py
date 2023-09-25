import json

# Script to create absolute path of the JSON file.

json_dir = input("please enter the json file you would like to parse ")

# Script to parse JSON

json = json.loads(open(json_dir).read())
value = json["name"]
print(value)

# Loop through JSON keys and values

for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))