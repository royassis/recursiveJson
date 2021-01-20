import json
import pandas as pd
from utils import rec

with open("sample.json", "r") as fp:
    data = json.load(fp)

result = rec(data)

df = pd.DataFrame(result)

print(df)
