import requests

pools_endpoint = "https://api.orca.so/allPools"

resp = requests.get( pools_endpoint )
data = resp.json()
for k,v in data.items(): 
   print( k, v )

