from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, distinct, update
from sqlalchemy import Table, Column, Integer, SMALLINT, String, MetaData, DateTime, BigInteger, TIMESTAMP, Boolean, DECIMAL, JSON, DATE
Base = declarative_base()
from sqlalchemy.sql import func

class DefiYieldPerformance(Base):
   __tablename__ = "defi_yield_performance"
   txn_time = Column(DateTime(timezone=False) , primary_key=True)
   partition_by_day = Column(SMALLINT)
   pool_address = Column(String)
   protocol_name = Column(String)
   yield_type = Column(String)
   price = Column(DECIMAL)
   tvl = Column(DECIMAL)
   vol_day = Column(DECIMAL)
   vol_week = Column(DECIMAL)
   vol_month = Column(DECIMAL)
   vol_tokena_day = Column(DECIMAL)
   vol_tokena_week = Column(DECIMAL)
   vol_tokena_month = Column(DECIMAL)
   vol_tokenb_day = Column(DECIMAL)
   vol_tokenb_week = Column(DECIMAL)
   vol_tokenb_month = Column(DECIMAL)
   fee_apr_day = Column(DECIMAL)
   fee_apr_week = Column(DECIMAL)
   fee_apr_month = Column(DECIMAL)
   rewarda_apr_day = Column(DECIMAL)
   rewarda_apr_week = Column(DECIMAL)
   rewarda_apr_month = Column(DECIMAL)
   rewardb_apr_day = Column(DECIMAL)
   rewardb_apr_week = Column(DECIMAL)
   rewardb_apr_month = Column(DECIMAL)
   total_apr_day = Column(DECIMAL)
   total_apr_week = Column(DECIMAL)
   total_apr_month = Column(DECIMAL)
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
   pool_address = Column(String)
   program_id = Column(String)
   action_type = Column(String)
   user_account = Column(String)
   token_mint_a = Column(String)
   token_mint_b = Column(String)
   amount_token_a = Column(DECIMAL)
   amount_token_b = Column(DECIMAL)
   transaction_signature = Column(String)


class DeFiSwapActivities(Base):
   __tablename__ = "defi_swap_activities"
   txn_time = Column(DateTime(timezone=False) , primary_key=True)
   program_address = Column(String)
   pool_address = Column(String)
   aggregator_address = Column(String)
   user_account = Column(String)
   source_mint = Column(String)
   destination_mint = Column(String)
   source_amount = Column(DECIMAL)
   destination_amount = Column(DECIMAL)
   transaction_signature = Column(String)

class DeFiProductMaster(Base):
   __tablename__ = "defi_product_master"
   product_id = Column(Integer, primary_key=True)
   product_type = Column(String)
   project_name = Column(String)
   pool_name = Column(String)
   pool_address = Column(String)
   token_a_name = Column(String)
   token_a_symbol = Column(String)
   token_a_address = Column(String)
   token_a_decimals = Column(SMALLINT)
   token_b_name = Column(String)
   token_b_symbol = Column(String)
   token_b_address = Column(String)
   token_b_decimals = Column(SMALLINT)
   inspection_date = Column(DateTime(timezone=False))
   lp_fee_rate = Column(DECIMAL)
   protocol_fee_rate = Column(DECIMAL)
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

