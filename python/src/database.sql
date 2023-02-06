CREATE TABLE defi_yield_performance (
   txn_time timestamp without time zone NOT NULL,
   partition_by_day smallint,
   pool_address VARCHAR ( 100 ), 
   protocol_name VARCHAR ( 30 ), 
   yield_type VARCHAR ( 10 ), 
   price decimal,
   tvl decimal,
   vol_day decimal,
   vol_week  decimal,
   vol_month decimal,
   vol_tokena_day decimal,
   vol_tokena_week decimal,
   vol_tokena_month  decimal,
   vol_tokenb_day decimal,
   vol_tokenb_week  decimal,
   vol_tokenb_month decimal,
   fee_apr_day decimal,
   fee_apr_week decimal,
   fee_apr_month decimal,
   rewardA_apr_day decimal,
   rewardA_apr_week decimal,
   rewardA_apr_month decimal,
   rewardB_apr_day decimal,
   rewardB_apr_week decimal,
   rewardB_apr_month decimal,
   total_apr_day decimal,
   total_apr_week decimal,
   total_apr_month decimal,
   pool_age int
);

CREATE TABLE defi_product_master
(
   product_id  serial PRIMARY KEY , 
   product_type varchar( 100 ),
   project_name varchar( 100 ),
   pool_name varchar( 100 ),
   pool_address varchar( 100 ),
   token_a_name varchar( 100 ),
   token_a_symbol varchar( 100 ),
   token_a_address varchar( 100 ),
   token_a_decimals smallint,
   token_b_name varchar( 100 ),
   token_b_symbol varchar( 100 ),
   token_b_address varchar( 100 ),
   token_b_decimals smallint,
   inspection_date date,
   protocol_fee_rate decimal,
   lp_fee_rate decimal,   
   created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()    
);
CREATE TABLE defi_pool_activities
(
    txn_time timestamp without time zone NOT NULL,
    program_id VARCHAR ( 64 ), 
    action_type VARCHAR ( 64 ), 
    user_account VARCHAR ( 64 ), 
    token_mint_a VARCHAR ( 64 ), 
    token_mint_b VARCHAR ( 64 ), 
    amount_token_a decimal,
    amount_token_b decimal,
    transaction_signature VARCHAR ( 120 ) ,
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()    
);

CREATE TABLE defi_swap_activities
(
    txn_time timestamp without time zone NOT NULL,
    program_address VARCHAR ( 64 ), 
    aggregator_address VARCHAR ( 64 ), 
    user_account VARCHAR ( 64 ), 
    source_mint VARCHAR ( 64 ), 
    destination_mint VARCHAR ( 64 ), 
    source_amount decimal,
    destination_amount decimal,
    transaction_signature VARCHAR ( 120 ) ,
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()    
);

CREATE TABLE defi_token_price
(
    txn_time timestamp without time zone NOT NULL,
    token VARCHAR ( 30 ), 
    price decimal,
    market_cap decimal,
    total_volume decimal
);

select * from defi_product_master  where pool_address = '7qbRF6YsyGuLUVs6Y1q64bdVrfe4ZcUUz1JRdoVNUJnm'
select * from defi_yield_performance where pool_address = '7qbRF6YsyGuLUVs6Y1q64bdVrfe4ZcUUz1JRdoVNUJnm'

-- get withdrawls and deposits
select token_mint_a, token_mint_b, action_type, DATE_TRUNC('hour', txn_time ) HOUR_OF_DAY , sum(amount_token_a)/1000000000 token_a, sum(amount_token_b)/1000000000  token_b
  from defi_pool_activities where token_mint_a = 'So11111111111111111111111111111111111111112'  
   and token_mint_b = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
 group by token_mint_a, token_mint_b, action_type, DATE_TRUNC('hour', txn_time )

-- get swaps 
select min(txn_time) , max(txn_time),  DATE_TRUNC('hour', txn_time ) HOUR_OF_DAY , source_mint, destination_mint, sum(source_amount/1000000000), sum(destination_amount/1000000000) 
  from defi_swap_activities group by  DATE_TRUNC('hour', txn_time ) , source_mint, destination_mint 
