import requests
import pandas as pd

url = "http://comp.fnguide.com/SVO2/common/lookup_data.asp?mkt_gb=1&comp_gb=1"
resp = requests.get(url)
data = resp.json()

df = pd.DataFrame(data=data)
df.head()