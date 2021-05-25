# API key 불러오기 
import ccxt 

with open("../api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

print(api_key)
print(secret)