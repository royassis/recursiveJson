import json
import pandas as pd
from utils import get_dict_list, get_flat_dict



def rec(mylist, base_dict, added_dict):
    dictlist = get_dict_list(base_dict)
    plain_dict = get_flat_dict(base_dict)

    if not dictlist:
        mylist.append(plain_dict | added_dict)
        return

    for newdict in dictlist:
        rec(mylist, newdict, plain_dict | added_dict)

    return mylist


with open("sample.json", "r") as fp:
    data = json.load(fp)

result = rec(list(), data, dict())

df = pd.DataFrame(result)

print(df)
