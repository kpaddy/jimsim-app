import requests
import json 
from data_models import DeFiPoolActivities
from sqlalchemy import create_engine, select, distinct, engine
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, BigInteger, TIMESTAMP, Boolean, DECIMAL, JSON, DATE
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.sql import func
from sqlalchemy.engine import make_url
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

RAY_SOL_USDC = {
         "program": "Raydium",
         "poolAddress": None,
         "poolName": "wSOL - USDC",
         "mintTokenA": "So11111111111111111111111111111111111111112",
         "nameTokenA": "Wrapped SOL",
         "mintTokenB": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
         "nameTokenB": "USD Coin",
         "tokenAccountA": "DQyrAcCrDXQ7NeoqGgDCZwBvWDcYmFCjSb9JtteuvPpz",
         "tokenAccountB": "HLmqeL62xR1QoZ1HKKbXRrdN1p3phKpxRMb2VVopvBBz",
         "balanceTokenALamports": "84202686073907",
         "balanceTokenBLamports": "2281329888328",
         "balanceTokenA": 84202.68607390701,
         "balanceTokenB": 2281329.888328
}

class DefiPoolActivitiesProcessor( object ):
   def __init__(self ) -> None:
      conn_string = 'postgresql://{}:{}@{}/{}'.format( os.getenv("db_user") , os.getenv("db_pass"), os.getenv("db_host"), os.getenv("db_name"))
      '''
      self.db  = create_engine(
            engine.url.URL(
            drivername=driver_name,
            username= os.getenv("db_user") ,
            password=os.getenv("db_pass"),
            database=os.getenv("db_name"),
            query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800)
      '''
      self.db = create_engine(conn_string)
      self._conn = self.db.connect()

   def save_activities_to_db(self, rows) :
      stmt = insert( DeFiPoolActivities, ).values(rows)    
      self._conn.execute(stmt)


RAY_RAY_USDC = {
         "program": "Raydium",
         "poolAddress": None,
         "poolName": "RAY - USDC",
         "mintTokenA": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
         "nameTokenA": "Raydium",
         "mintTokenB": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
         "nameTokenB": "USD Coin",
         "tokenAccountA": "FdmKUE4UMiJYFK5ogCngHzShuVKrFXBamPWcewDr31th",
         "tokenAccountB": "Eqrhxd7bDUCH3MepKmdVkgwazXRzY6iHhEoBpY7yAohk",
         "balanceTokenALamports": "5878212475792",
         "balanceTokenBLamports": "1377760214558",
         "balanceTokenA": 5878212.475792,
         "balanceTokenB": 1377760.214558
      }

#jan21
EPOCTIME = 1674309533

def get_pool_withdrawls_deposits( token1, token2, t1, t2 ):
   url = "https://rest-api.hellomoon.io/v0/defi/liquidity-pools/withdrawals-deposits"
   payload = {
      "tokenMintA": token1,
      "tokenMintB": token2
   }   
   headers = {
         "accept": "application/json",
      "content-type": "application/json",
      "authorization": "Bearer 768ea71c-f3e5-43eb-8b1e-7c8b0109eef7"
   }
   response = requests.post(url, json=payload, headers=headers)
   outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_w_d.json", 'w')
   json.dump ( response.json(), outfile )
   data = response.json()
   new_recs = []
   mapping = {'programId':'program_id', 'actionType':'action_type', 'blockTime':'txn_time', 'userAccount':'user_account', 'tokenMintA':'token_mint_a', 'tokenMintB':'token_mint_b', 'amountTokenA':'amount_token_a', 'amountTokenB':'amount_token_b' , 'transactionId':'transaction_signature'}
   for row in data["data"] :
      newrow = { v : row[k] for k,v in mapping.items() }
      newrow['txn_time'] = datetime.fromtimestamp( int(newrow['txn_time']) )
      new_recs.append( newrow )
      print( newrow['transaction_signature'])
   DefiPoolActivitiesProcessor().save_activities_to_db( new_recs )


def get_pool_emissions( pool_address, t1, t2 ):
   url = "https://rest-api.hellomoon.io/v0/defi/liquidity-pools/emissions"
   payload = {"poolAddress": pool_address }
   headers = {
         "accept": "application/json",
      "content-type": "application/json",
      "authorization": "Bearer 768ea71c-f3e5-43eb-8b1e-7c8b0109eef7"
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
      "authorization": "Bearer 768ea71c-f3e5-43eb-8b1e-7c8b0109eef7"
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
      "authorization": "Bearer 768ea71c-f3e5-43eb-8b1e-7c8b0109eef7"
   }
   response = requests.post(pool_balance_endpoint, json=payload, headers=headers)
   outfile = open(f"../data/hellomoon_orca_{t1}-{t2}_pool_balance.json", 'w')
   json.dump ( response.json(), outfile )
   return response.json()

#response = get_ray_pool_balances( SOL, USDC, 'SOL', 'USDC' )
#response = get_ray_pool_balances( RAY, USDC, 'RAY' , 'USDC' )
#response = get_orca_pool_balances( ORCA_MSOL_USDC, 'mSOL', 'USDC' )
#response = get_orca_pool_balances( ORCA_SOL_USDC, 'SOL', 'USDC' )

get_pool_emissions( ORCA_STSOL_SOL, 'stSOL', 'SOL' ) 
get_pool_emissions( ORCA_SLCL_USDC, 'SLCL', 'USDC' )

#get_pool_withdrawls_deposits(SOL, USDC, 'SOL', 'USDC')


#Wrapped SOL ==> So11111111111111111111111111111111111111112
#USDC ==> EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
