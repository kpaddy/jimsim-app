import requests
import json 
from data_models import DeFiPoolActivities, DeFiSwapActivities
from sqlalchemy import create_engine 
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.sql import func
from datetime import datetime 
import os 

SOL = "So11111111111111111111111111111111111111112"
USDC = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
RAY = "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R"
USDT = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
MSOL_USDT = "Afvh7TWfcT1E9eEEWJk17fPjnqk36hreTJJK5g3s4fm8"

ORCA_MSOL_USDC = "HJPjoWUrhoZzkNfRpHuieeFk9WcZWjwy6PBjZ81ngndJ"
ORCA_SOL_USDC = "FFdjrSvNALfdgxANNpt3x85WpeVMdQSH5SEP2poM8fcK"
ORCA_USDC_USDT = "GjpXgKwn4VW4J2pZdS3dovM58hiXWLJtopTfqG83zY2f"
ORCA_SLCL_USDC = "8Gbr3TGdVhEABN52yxBqUfLxMXQqh8KRuEb44joHwHAN"
ORCA_STSOL_SOL = "2AEWSvUds1wsufnsDPCXjFsJCMJH5SNNm7fSF4kxys9a"

pool_balance_endpoint = "https://rest-api.hellomoon.io/v0/defi/liquidity-pools/balances"

class DefiPoolActivitiesProcessor( object ):
   def __init__(self ) -> None:
      conn_string = 'postgresql://{}:{}@{}/{}'.format( os.getenv("db_user") , os.getenv("db_pass"), os.getenv("db_host"), os.getenv("db_name"))
      self.db = create_engine(conn_string)
      self._conn = self.db.connect()

   def save_activities_to_db(self, rows) :
      stmt = insert( DeFiPoolActivities, ).values(rows)    
      self._conn.execute(stmt)

   def save_swaps_to_db(self, rows) :
      stmt = insert( DeFiSwapActivities, ).values(rows)    
      self._conn.execute(stmt)

#jan21
EPOCTIME = 1674309533

def get_pool_withdrawls_deposits( token1, token2, t1, t2, pool_address ):
   url = "https://rest-api.hellomoon.io/v0/defi/liquidity-pools/withdrawals-deposits"
   payload = {
      "tokenMintA": token1,
      "tokenMintB": token2,
      "limit": 100

   }   
   headers = {
         "accept": "application/json",
      "content-type": "application/json",
      "authorization": os.getenv("hellomoon_api_key")
   }
   response = requests.post(url, json=payload, headers=headers)
   #outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_w_d.json", 'w')
   #json.dump ( response.json(), outfile )
   data = response.json()
   new_recs = []
   mapping = {'programId':'program_id', 'actionType':'action_type', 'blockTime':'txn_time', 'userAccount':'user_account', 'tokenMintA':'token_mint_a', 'tokenMintB':'token_mint_b', 'amountTokenA':'amount_token_a', 'amountTokenB':'amount_token_b' , 'transactionId':'transaction_signature'}
   for row in data["data"] :
      newrow = { v : row[k] for k,v in mapping.items() }
      newrow['txn_time'] = datetime.fromtimestamp( int(newrow['txn_time']) )
      newrow['pool_address'] = pool_address
      new_recs.append( newrow )
      #print( newrow['transaction_signature'])
   if len(new_recs) > 0:
      print(f"Save {len(new_recs)} records to defi_pool_activities table ")
      DefiPoolActivitiesProcessor().save_activities_to_db( new_recs )

def get_swaps_records( token1, token2, pool_address ):
   url = "https://rest-api.hellomoon.io/v0/defi/swaps"
   payload = {
      "sourceMint": token1,
      "destinationMint": token2,
      "limit": 100,
      "programId": "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc"

   }   
   headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": os.getenv("hellomoon_api_key")
   }
   response = requests.post(url, json=payload, headers=headers)
   #outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_w_d.json", 'w')
   #json.dump ( response.json(), outfile )
   data = response.json()
   new_recs = []
   mapping = {'userAccount':'user_account', 'sourceMint':'source_mint', 'destinationMint':'destination_mint', 
      'programId':'program_address', 'aggregatorId':'aggregator_address', 'sourceAmount':'source_amount', 'destinationAmount':'destination_amount', 'blockTime':'txn_time' , 'transactionId':'transaction_signature'}
   for row in data["data"] :
      newrow = { v : row[k] for k,v in mapping.items() }
      newrow['txn_time'] = datetime.fromtimestamp( int(newrow['txn_time']) )
      newrow['pool_address'] = pool_address

      new_recs.append( newrow )
      #print( newrow['transaction_signature'])
   if len(new_recs) > 0:
      print(f"Save {len(new_recs)} swap records to defi_swap_activities table ")
      DefiPoolActivitiesProcessor().save_swaps_to_db( new_recs )

def get_pool_emissions( pool_address, t1, t2 ):
   url = "https://rest-api.hellomoon.io/v0/defi/liquidity-pools/emissions"
   payload = {"poolAddress": pool_address }
   headers = {
         "accept": "application/json",
      "content-type": "application/json",
      "authorization": os.getenv("hellomoon_api_key")
   }
   response = requests.post(url, json=payload, headers=headers)
   outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_emissions.json", 'w')
   json.dump ( response.json(), outfile )

def get_ray_pool_balances( tokenA, tokenB, t1, t2):
   payload = {
      "mintTokenA": tokenA,
      "mintTokenB": tokenB
   }
   headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": os.getenv("hellomoon_api_key")
   }
   response = requests.post(pool_balance_endpoint, json=payload, headers=headers)
   outfile = open(f"../data/hellomoon_ray_{t1}-{t2}_pool_balance.json", 'w')
   json.dump ( response.json(), outfile )
   return response.json()


def get_orca_pool_balances( pool_address, t1, t2):
   payload = {
      "poolAddress": pool_address 
   }
   headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": os.getenv("hellomoon_api_key")
   }
   response = requests.post(pool_balance_endpoint, json=payload, headers=headers)
   outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_balance.json", 'w')
   json.dump ( response.json(), outfile )
   return response.json()

#response = get_ray_pool_balances( SOL, USDC, 'SOL', 'USDC' )
#response = get_ray_pool_balances( RAY, USDC, 'RAY' , 'USDC' )
#response = get_orca_pool_balances( ORCA_MSOL_USDC, 'mSOL', 'USDC' )
#response = get_orca_pool_balances( ORCA_SOL_USDC, 'SOL', 'USDC' )

#get_pool_emissions( ORCA_STSOL_SOL, 'stSOL', 'SOL' ) 
#get_pool_emissions( ORCA_SLCL_USDC, 'SLCL', 'USDC' )
pool_address = '7qbRF6YsyGuLUVs6Y1q64bdVrfe4ZcUUz1JRdoVNUJnm'
get_pool_withdrawls_deposits(SOL, USDC, 'SOL', 'USDC', pool_address)
get_swaps_records(SOL, USDC, pool_address)
#Wrapped SOL ==> So11111111111111111111111111111111111111112
#USDC ==> EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
