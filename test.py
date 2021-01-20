import json
from utils import unravel_nested_dict

with open("sample.json", "r") as fp:
    data = json.load(fp)

result = unravel_nested_dict(data)

print(result)
