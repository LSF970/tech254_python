# Parsing is making something (more) understandable. So let's make json more understandable for Python.

import json
parsed_json = json.loads(open("example_json.json").read())
print(type(parsed_json))
value = parsed_json["website"]
print(value)

