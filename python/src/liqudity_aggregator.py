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
orca_whirlpools_endpoint = "https://api.mainnet.orca.so/v1/whirlpool/list"
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
      pass
   def get_auqafarm_pool_stats(self):
      data = fetch_data( orca_pools_endpoint )
      #repsonse = [self.transform(v) for v in data.values()]
      return data 

   def save_whirlpool_master_data_to_db(self):
      orca_data = fetch_data( orca_whirlpools_endpoint )
      #orca_file = open("../samples/orca_whirlpool_stats.json", 'w')
      #json.dump(orca_data, orca_file)
      db_recs = []
      for item in orca_data["whirlpools"]:
         pool_name = f"{item['tokenA']['symbol']}-{item['tokenB']['symbol']}"
         db_rec = {
         'product_type':'LiquidityPool' , 'project_name':'ORCA-Whirlpools', 
         'pool_name': pool_name, 'pool_address':item['address'], 
         'token_a_name':item['tokenA']['name'], 'token_a_symbol':item['tokenA']['symbol'], 'token_a_address':item['tokenA']['mint'], 'token_a_decimals':item['tokenA']['decimals'], 
         'token_b_name':item['tokenB']['name'], 'token_b_symbol':item['tokenB']['symbol'], 'token_b_address':item['tokenB']['mint'], 'token_b_decimals':item['tokenB']['decimals'],
         'inspection_date':None, 'lp_fee_rate':item['lpFeeRate'] , 'protocol_fee_rate':item['protocolFeeRate']     }
         db_recs.append(db_rec)
      DeFiDBProcessor().save_product_master( db_recs  )

   def save_whirlpool_stats_data_to_db(self):
      orca_data = fetch_data( orca_whirlpools_endpoint )
      performance_rows = []
      for item in orca_data["whirlpools"]:
         if 'tvl' not in item:
            continue
         rec = {
            'txn_time' : datetime.now() , 
            'partition_by_day' : datetime.now().day,
            'pool_address' : item['address'], 
            'protocol_name' : 'ORCA-Whirlpools',
            'yield_type' : 'LP', 
            'price' : item['price'],
            'tvl' : item['tvl'], 
            'vol_day' : item['volume']['day'],
            'vol_week' : item['volume']['week'],
            'vol_month' : item['volume']['month'],
            'vol_tokena_day' : item['volumeDenominatedA']['day'],
            'vol_tokena_week' : item['volumeDenominatedA']['week'],
            'vol_tokena_month' : item['volumeDenominatedA']['month'],
            'vol_tokenb_day' :  item['volumeDenominatedB']['day'],
            'vol_tokenb_week' : item['volumeDenominatedB']['week'],
            'vol_tokenb_month' :  item['volumeDenominatedB']['month'],
            'fee_apr_day' :  item['feeApr']['day'],
            'fee_apr_week' :  item['feeApr']['week'],
            'fee_apr_month' :  item['feeApr']['month'],
            'rewarda_apr_day' :  item['feeApr']['day'],
            'rewarda_apr_week' :  item['feeApr']['week'],
            'rewarda_apr_month' :  item['reward0Apr']['month'],
            'rewardb_apr_day' :  item['reward1Apr']['day'],
            'rewardb_apr_week' :  item['reward1Apr']['week'],
            'rewardb_apr_month' :  item['reward1Apr']['month'],
            'total_apr_day' : item['totalApr']['day'],
            'total_apr_week' : item['totalApr']['week'],
            'total_apr_month' : item['totalApr']['month'],
            'pool_age' : None
         }
         performance_rows.append( rec )
      DeFiDBProcessor().save_pool_performance_to_db( performance_rows   )


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

async def save_to_db( ):
   '''
   rows = await transform_to_db( rows )
   print(f"total records {len(rows)}")
   db = DeFiDBProcessor( )
   db.save_pool_performance_to_db( rows )
   #OrcaProcessor().save_whirlpool_master_data_to_db()
   '''
   #OrcaProcessor().save_whirlpool_master_data_to_db()
   OrcaProcessor().save_whirlpool_stats_data_to_db()

async def fetch_all_data( ):
   #radiyum_task = asyncio.create_task( RadiyumProcessor().get_pool_stats() )
   #orca_task = asyncio.create_task( OrcaProcessor().get_pool_stats() )
   #lifinity_task = asyncio.create_task( LifinityProcessor().get_pool_stats() )
   #reponse_list = await asyncio.gather( *[radiyum_task, orca_task, lifinity_task] )
   #data = list(chain(*reponse_list))
   #print(len(data))
   #await save_to_db( data )
   await save_to_db()

def run():
   try:
      respose_data =  asyncio.run( fetch_all_data() )
      return respose_data
   except:
      print('error')
      return []

run()