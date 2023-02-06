import requests
import json 
from collections  import defaultdict
import pandas as pd
yields_endpoint = "https://yields.llama.fi/pools"
protocols_endpoint = "https://api.llama.fi/protocols"

solana_tokens_endpoint_1 = "https://raw.githubusercontent.com/solana-labs/token-list/main/src/tokens/solana.tokenlist.json"
solana_tokens_endpoint_2 = "https://cdn.jsdelivr.net/gh/solana-labs/token-list@latest/src/tokens/solana.tokenlist.json"

def refresh_pools_data():
   resp = requests.get( yields_endpoint )
   data = resp.json()
   outfile = open("pools_response_20230125_1207.json", "w")
   json.dump(data, outfile)

def read_pools_data():
   outfile = open("pools_response_20230125_1207.json", "r")
   data = json.load( outfile )
   return data 

def load_chain_data():
   resp = requests.get( protocols_endpoint )
   data = resp.json()
   outfile = open("chains_response_20230125_1249.json", "w")
   json.dump(data, outfile)

def read_chains_data():
   outfile = open("chains_response_20230125_1249.json", "r")
   data = json.load( outfile )
   return data 

def write_sol_pools():
   data = read_pools_data()
   #solana_pools = [ d for d in data["data"] if d["chain"] == "Solana"]
   df =  pd.DataFrame( data["data"] )
   df2 = df.groupby(['chain']).count().sort_values( by=["symbol"] , ascending=False)
   print( df2 )
   df.loc[ df["chain"] == "Solana"].to_csv("solana_pools.csv", index=False)

#data = read_chains_data()
'''
solana_projects = [ d for d in data  if "Solana" in d["chains"] ]
sol_tvls = []
for p in solana_projects:
   if len(p['chainTvls']) > 0 and list(p['chainTvls'].values())[0] > 0:
      sol_tvls.append( p )
df = pd.DataFrame( p )
df.to_csv("solana_chains.csv", index=False)
'''
#df = pd.DataFrame( data )
#df.loc[ df["chain"] == "Solana"].to_csv("solana_chains.csv", index=False)

#df2 = df.groupby(['chain']).count().sort_values( by=["symbol"] , ascending=False)
resp = requests.get(solana_tokens_endpoint_2)
data = resp.json()
print(f'Solana has {len(data["tokens"])} tokens ')
lifinty_tokens = [t for t in data["tokens"] if "lifinity"in t["name"].lower() ]
for t in lifinty_tokens:
   print( t )
   #break