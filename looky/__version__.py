import os

here = os.path.abspath(os.path.dirname(__file__))
top = os.path.dirname(here)

with open(os.path.join(top, "API_key.txt"), "r") as f:
    API_KEY = f.readline()
