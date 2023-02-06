CREATE TABLE defi_product_master
(
   product_id  serial PRIMARY KEY , 
   product_type varchar( 100 ),
   project_name varchar( 100 ),
   pool_name varchar( 100 ),
   pool_address varchar( 100 ),
   token_a_name varchar( 100 ),
   token_a_ticker varchar( 100 ),
   token_a_address varchar( 100 ),
   token_b_name varchar( 100 ),
   token_b_ticker varchar( 100 ),
   token_b_address varchar( 100 ),
   inspection_date date,
   fee_rate decimal,
   data_provider varchar( 100 ),
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

CREATE TABLE defi_token_price
(
    txn_time timestamp without time zone NOT NULL,
    token VARCHAR ( 40 ), 
    price decimal,
    market_cap decimal,
    total_volume decimal,
    data_provider varchar( 100 ),
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()    
); 

CREATE TABLE defi_yield_performance
(
    txn_time timestamp without  time zone NOT NULL,
    partition_by_day smallint,
    pair_id VARCHAR ( 30 ), 
    protocol_id VARCHAR ( 30 ),
    yield_type VARCHAR ( 10 ), 
    apy_rate decimal, 
    tvl float, 
    vol BIGINT,
    apy_history decimal, 
    tvl_history float, 
    vol_history BIGINT,
    pool_age Int
    
)
PARTITION BY RANGE (partition_by_day);

CREATE TABLE defi_yield_performance_part_1 PARTITION OF defi_yield_performance
    FOR VALUES FROM (1) TO (10);
CREATE INDEX idx_defi_yield_performance_part_1 ON defi_yield_performance_part_1(partition_by_day);

CREATE TABLE defi_yield_performance_part_2 PARTITION OF defi_yield_performance
    FOR VALUES FROM (11) TO (20);
CREATE INDEX idx_defi_yield_performance_part_2 ON defi_yield_performance_part_2(partition_by_day);

CREATE TABLE defi_yield_performance_part_3 PARTITION OF defi_yield_performance
    FOR VALUES FROM (21) TO (30);
CREATE INDEX idx_defi_yield_performance_part_3 ON defi_yield_performance_part_3(partition_by_day);

CREATE TABLE defi_yield_performance_part_4 PARTITION OF defi_yield_performance
    FOR VALUES FROM (31) TO (40);
CREATE INDEX idx_defi_yield_performance_part_4 ON defi_yield_performance_part_4(partition_by_day);
CREATE INDEX idx_defi_yield_performance_1 ON  defi_yield_performance(txn_time, pair_id, protocol_id );
