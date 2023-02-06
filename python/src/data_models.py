from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, distinct, update
from sqlalchemy import Table, Column, Integer, SMALLINT, String, MetaData, DateTime, BigInteger, TIMESTAMP, Boolean, DECIMAL, JSON, DATE
Base = declarative_base()
from sqlalchemy.sql import func

class GameActivitiesTxn(Base):
   __tablename__ = "sol_game_activities_txn"
   activity_id = Column(Integer, primary_key=True)
   project_id = Column(SMALLINT)
   program_id = Column(SMALLINT)
   primary_activity_type_id = Column(SMALLINT)   
   activity_type_id = Column(SMALLINT)   
   instruction_id =  Column(SMALLINT)   
   player_address = Column(String)
   source_address = Column(String)
   desti_address = Column(String)
   mint_address = Column(String)
   owner_address = Column(String)
   wallet_address = Column(String)
   amount = Column(Integer)
   slot = Column(Integer)
   txn_dt = Column(DateTime(timezone=False))
   created_at = Column(DateTime(timezone=False), server_default=func.now())


class DefiYieldPerformance(Base):
   __tablename__ = "defi_yield_performance"
   txn_time = Column(DateTime(timezone=False) , primary_key=True)
   partition_by_day = Column(SMALLINT)
   pair_id = Column(String)
   protocol_id = Column(String)
   yield_type = Column(String)
   apy_rate = Column(DECIMAL)
   tvl = Column(DECIMAL)
   vol = Column(BigInteger)
   apy_history = Column(DECIMAL)
   tvl_history = Column(DECIMAL)
   vol_history = Column(BigInteger)
   pool_age = Column(Integer)

class DeFiTokenPrice(Base):
   __tablename__ = "defi_token_price"
   txn_time = Column(DateTime(timezone=False) , primary_key=True)
   token = Column(String)
   price = Column(DECIMAL)
   market_cap = Column(DECIMAL)
   total_volume = Column(DECIMAL)

class DeFiPoolActivities(Base):
   __tablename__ = "defi_pool_activities"
   txn_time = Column(DateTime(timezone=False) , primary_key=True)
   program_id = Column(String)
   action_type = Column(String)
   user_account = Column(String)
   token_mint_a = Column(String)
   token_mint_b = Column(String)
   amount_token_a = Column(DECIMAL)
   amount_token_b = Column(DECIMAL)
   transaction_signature = Column(String)


class DeFiProductMaster(Base):
   __tablename__ = "defi_product_master"
   product_id = Column(Integer, primary_key=True)
   product_type = Column(String)
   project_name = Column(String)
   pool_name = Column(String)
   pool_address = Column(String)
   token_a_name = Column(String)
   token_a_ticker = Column(String)
   token_a_address = Column(String)
   token_b_name = Column(String)
   token_b_ticker = Column(String)
   token_b_address = Column(String)
   inspection_date = Column(DateTime(timezone=False))
   fee_rate = Column(DECIMAL)
   created_at = Column(DateTime(timezone=False), server_default=func.now())

class DeFiPoolEmissions(Base):
   __tablename__ = "defi_pool_emissions"
   emission_id = Column(Integer, primary_key=True)
   txn_time = Column(DateTime(timezone=False))
   project_name = Column(String)
   pool_name = Column(String)
   pool_address = Column(String)
   mint_address = Column(String)
   emissions_per_day = Column(String)

