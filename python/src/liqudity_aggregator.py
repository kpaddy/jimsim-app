#import functions_framework
import requests
import re
from datetime import datetime
import asyncio
from itertools import chain
import cachetools.func
import json 
import os 
from sqlalchemy import create_engine 
from data_models import DefiYieldPerformance, DeFiProductMaster
from sqlalchemy.dialects.postgresql import insert

pat = r'.*?\[(.*)].*'
orca_pools_endpoint = "https://api.orca.so/allPools"
lifinity_pools_endpoint = "https://lifinity.io/api/poolinfo"
radiyum_pools_endpoint = "https://api.raydium.io/v2/main/pairs"

class DeFiDBProcessor( object ):
   def __init__(self ) -> None:
      conn_string = 'postgresql://{}:{}@{}/{}'.format( os.getenv("db_user") , os.getenv("db_pass"), os.getenv("db_host"), os.getenv("db_name"))
      self.db = create_engine(conn_string)
      self._conn = self.db.connect()

   def save_pool_performance_to_db(self, rows) :
      stmt = insert( DefiYieldPerformance, ).values(rows)    
      self._conn.execute(stmt)

   def save_product_master( self, rows ):
      stmt = insert( DeFiProductMaster, ).values(rows)    
      self._conn.execute(stmt)


def fetch_data( end_point ):
   resp = requests.get( end_point )
   return resp.json() 

def calculate_age( date_str, date_format='%Y/%m/%d'):
   delta = datetime.utcnow() - datetime.strptime( date_str, date_format) 
   return delta.days

class LifinityProcessor(object):
   def __init__(self) -> None:
      pass

   #{'symbol': 'GMT-USDC', 'volume7Days': 193214.068274, 'volume7DaysX': 172090.757084454, 'volume7DaysY': 97689.677632, 'volumeYesterDay': 19233.478618, 'volumeYesterDayX': 15944.543677939, 'volumeYesterDayY': 9473.127303, 'fee': 139.89017764420694, 'netapr': 225.2700034660432, 'ca': 85.5597566829423, 'startDate': '2022/06/13', 'coinBalance': 9184715624664, 'pcBalance': 5271565598, 'liquidity': '$10,843.73', 'liquidityAmount': 10843.732983613125, 'pythPrice': 0.60667827, 'pythPcPrice': 1}
   def transform(self, rec):

      newdoc = {'pair': rec['symbol'], 'protocol':'LIFINITY', 'yield_type':'POOL', 'apy_info':'coming soon',
         'apy': rec['netapr'] , 'apy_history':None,  'pool_age': calculate_age( rec['startDate']), 
         'tvl': rec['liquidityAmount'], 'tvl_history':None,
         'vol': rec['volumeYesterDay'], 'vol_history':None}
      return newdoc 

   async def get_pool_stats(self):
      data = fetch_data( lifinity_pools_endpoint )
      repsonse = [self.transform(v) for v in data ]
      return repsonse 

class OrcaProcessor(object):
   def __init__(self) -> None:
      pass
   def transform(self, rec):
      #print( "rec['poolId'] ", rec['poolId'] )
      if "[" in rec['poolId']:
         market = re.search(pat, rec['poolId']).group(1)
         pair = rec['poolId'][0:rec['poolId'].find('[')].replace("/", '_')
         protocol = "ORCA-" + market.capitalize()
      else:
         pair = rec['poolId'].replace("/", '_')
         protocol = "ORCA"

      newdoc = {'pair': pair, 'protocol':protocol, 'yield_type':'POOL', 'apy_info':'coming soon',
         'apy': round( float(rec['apy']['month'])*100 , 3) , 'apy_history':0,  'pool_age':None, 
         'tvl': int(rec['poolTokenSupply']), 'tvl_history':None,
         'vol': float(rec['volume']['day']), 'vol_history':None}
      return newdoc 

   async def get_pool_stats(self):
      data = fetch_data( orca_pools_endpoint )
      repsonse = [self.transform(v) for v in data.values()]
      return repsonse 

class RadiyumProcessor(object):
   def __init__(self) -> None:
      pass

   def transform(self, rec):
      pair = rec["name"].replace("-", "-")
      newdoc = {'pair': pair, 'protocol':'RADIYUM', 'yield_type':'POOL', 'apy_info':'coming soon',
         'apy': rec['apr24h']  , 'apy_history':0,  'pool_age':None, 
         'tvl': rec['liquidity'], 'tvl_history':None,
         'vol': rec['volume24h'], 'vol_history':None}
      return newdoc 

   async def get_pool_stats(self):
      data = fetch_data( radiyum_pools_endpoint )
      #outfile = open("radiyum_sample.json", 'w')
      #json.dump(  data , outfile)
      repsonse = [self.transform(v) for v in data ]
      return repsonse 

async def transform_to_db(rows):
   #{'pair': 'SHIVX-USDC', 'protocol': 'RADIYUM', 'yield_type': 'POOL',
   #    'apy_info': 'coming soon', 'apy': 0, 'apy_history': 0, 'pool_age': None, 
   #    'tvl': 21.895466, 'tvl_history': None, 'vol': 0, 'vol_history': None}, 
   result_list = []
   for rec in rows:
      if (rec['tvl'] <= 1.0 and rec['vol'] <= 1 ) or ( rec['pair'].startswith('unknown') ):
         continue
      curr_time = datetime.utcnow()
      newrow = { 'txn_time':curr_time, 'partition_by_day' :curr_time.day, 
         'pair_id':rec['pair'], 'protocol_id':rec['protocol'], 
         'yield_type':rec['yield_type'], 'apy_rate':rec['apy'],  'tvl':rec['tvl'], 'vol':rec['vol'] ,
         'apy_history':rec['apy_history'],  'tvl_history':rec['tvl_history'], 'vol_history':rec['vol_history'] ,
         'pool_age':rec['pool_age'] }
      result_list.append( newrow )
   return result_list

async def save_to_db( rows ):
   rows = await transform_to_db( rows )
   print(f"total records {len(rows)}")
   db = DeFiDBProcessor( )
   db.save_pool_performance_to_db( rows )
   #db.save_pool_performance_to_db( rows[2000:] )
   #names = [r['protocol_id'] for r in rows[4500:]]
   #print( names )

async def fetch_all_data( ):
   radiyum_task = asyncio.create_task( RadiyumProcessor().get_pool_stats() )
   orca_task = asyncio.create_task( OrcaProcessor().get_pool_stats() )
   lifinity_task = asyncio.create_task( LifinityProcessor().get_pool_stats() )
   reponse_list = await asyncio.gather( *[radiyum_task, orca_task, lifinity_task] )
   data = list(chain(*reponse_list))
   print(len(data))
   await save_to_db( data )


def run():
   try:
      respose_data =  asyncio.run( fetch_all_data() )
      return respose_data
   except:
      print('error')
      return []

def save_master_data( ):
   row1 = { 'product_type':'LiquidityPool' , 'project_name':'ORCA', 
      'pool_name':'stSOL-SOL', 'pool_address':'2AEWSvUds1wsufnsDPCXjFsJCMJH5SNNm7fSF4kxys9a', 
      'token_a_name':'Lido SOL', 'token_a_ticker':'stSOL', 'token_a_address':'orcaEKTdK7LKz57vaAYr9QeNsVEPfiu6QeMU1kektZE',
      'token_b_name':'Orca SOL', 'token_b_ticker':'SOL', 'token_b_address':'HZRCwxP2Vq9PCpPXooayhJ2bxTpo5xfpQrwB1svh332p', 
      'inspection_date':None, 'fee_rate':0.01} 

   row2 = { 'product_type':'LiquidityPool' , 'project_name':'ORCA', 
      'pool_name':'SLCL-USDC', 'pool_address':'8Gbr3TGdVhEABN52yxBqUfLxMXQqh8KRuEb44joHwHAN', 
      'token_a_name':'Social Token', 'token_a_ticker':'SLCL', 'token_a_address':'SLCLww7nc1PD2gQPQdGayHviVVcpMthnqUz2iWKhNQV',
      'token_b_name':'Orca', 'token_b_ticker':'USDC', 'token_b_address':'orcaEKTdK7LKz57vaAYr9QeNsVEPfiu6QeMU1kektZE', 
      'inspection_date':None, 'fee_rate':0.3} 

   DeFiDBProcessor().save_product_master( [row1, row2] )

@cachetools.func.ttl_cache(maxsize=10000, ttl=2 * 60)
def retrive_data():
   return run()   
 
save_master_data()

'''
@functions_framework.http
def hello_http(request):
   request_json = request.get_json(silent=True)   
   return {"data": retrive_data() }

run()
'''
#asyncio.run(  RadiyumProcessor().get_pool_stats() )
#asyncio.run(  fetch_all_data() )



