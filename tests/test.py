import json
from recursiveJson.utils import unravel_nested_dict
from pathlib import Path
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

current_dir = Path(__file__).parent
# p = current_dir.joinpath("out.json")
p = r"C:\Users\Roy\PycharmProjects\recursiveJson\tests\out.json"

with open(p, "r") as fp:
    data = json.load(fp)

flat_df = unravel_nested_dict(data)
print(flat_df)
flat_df.to_csv(r"C:\Users\Roy\PycharmProjects\recursiveJson\data\results\results.csv")

# print()
#
# multiple_seperate_dfs = nested_dict_to_model(data)
# for df in multiple_seperate_dfs:
#     print(df)

