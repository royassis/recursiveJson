import json
from utils import unravel_nested_dict, nested_dict_to_model

with open("sample.json", "r") as fp:
    data = json.load(fp)

one_flat_df = unravel_nested_dict(data)
print(one_flat_df)

multiple_seperate_dfs = nested_dict_to_model(data)
for df in multiple_seperate_dfs:
    print(df)
