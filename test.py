import json
from utils import unravel_nested_dict, nested_dict_to_model_base

with open("sample.json", "r") as fp:
    data = json.load(fp)

# result = unravel_nested_dict(data)
# print(result)


result = nested_dict_to_model_base(list(), data)
print(result)