import json
from recursiveJson.utils import unravel_nested_dict, nested_dict_to_model
from pathlib import Path
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

current_dir = Path(__file__).parent
p = current_dir.joinpath("out.json")

with open(p, "r") as fp:
    data = json.load(fp)


one_flat_df = unravel_nested_dict(data)
print(one_flat_df)

# print()
#
# multiple_seperate_dfs = nested_dict_to_model(data)
# for df in multiple_seperate_dfs:
#     print(df)

