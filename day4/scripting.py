# Scripting

# There are seven modules that we can consider "core" in Python.

import sys
import os
import subprocess
import math
from random import randrange
from datetime import datetime

import json

# sys

print(sys.version)

# os

# print(os.getcwd())
#
#
#
# os.mkdir("test_dir")

# subprocess

subprocess.run(["python", "hello_world.py"])

# math

pi = math.pi
pi_string = str(pi)
print(f"The value of pi is {pi_string}")

# random

rand_num = randrange(1, 10)
print(rand_num)

# datetime

whatisthedate = datetime.now()
print(whatisthedate)

# json

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
print(type(y))
