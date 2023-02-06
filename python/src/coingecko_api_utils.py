import defi.defi_tools as dft
import pandas as pd
import requests 
import json 
import os 
from sqlalchemy import create_engine 
from data_models import DeFiTokenPrice
from sqlalchemy.dialects.postgresql import insert

all_protocols_endpoint = "https://api.llama.fi/protocols"
get_protocol_endpoint = "https://api.llama.fi/protocol/{protocol}"

class TokenHistoryPriceProcessor( object ):
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

   def save_price_to_db(self, rows) :
      stmt = insert( DeFiTokenPrice, ).values(rows)    
      self._conn.execute(stmt)



def geckoList(page=1, per_page=250):
    """Returns list of full detail conGecko currency list
    
    Args:
        page (int, optional): number of pages
        per_page (int, optional): number of records per page
    
    Returns:
        DataFrame: list of full detail conGecko currency list
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency":"usd", "order":"market_cap_desc", "per_page":per_page, "page":page}
    r = requests.get(url, params).json()
    df = pd.DataFrame(r)
    df.set_index('symbol', inplace=True)
    return df


def geckoHistorical(ticker, token_name, vs_currency='usd', days='max'):
    """Historical prices from coinGecko
    
    Args:
        ticker (string): gecko ID, ie "bitcoin"
        vs_currency (str, optional): ie "usd" (default)
        days (str, optional): ie "20", "max" (default)
    
    Returns:
        DataFrame: Full history: date, price, market cap & volume
    """
    
    url = f"https://api.coingecko.com/api/v3/coins/{token_name}/market_chart"
    params = {"vs_currency":{vs_currency}, "days":days}
    r = requests.get(url, params).json()
    print( r.keys() )
    outfile = open("../data/sol_historical_gecko" + token_name +".json", 'w')
    json.dump( r , outfile )
    prices = pd.DataFrame(r['prices'])
    market_caps = pd.DataFrame(r['market_caps'])
    total_volumes = pd.DataFrame(r['total_volumes'])
    df = pd.concat([prices, market_caps[1], total_volumes[1]], axis=1)
    df[0] = pd.to_datetime(df[0], unit='ms')
    df.columns = ['date','price','market_caps','total_volumes']
    df.rename(columns = {'date':'txn_time',  'market_caps':'market_cap', 'total_volumes':'total_volume'}, inplace = True)
    df.set_index('txn_time', inplace=True)
    df['token'] = ticker
    df.to_csv("../data/sol_historical_gecko" + ticker +".csv")
    #return df
    #TokenHistoryPriceProcessor().save_price_to_db( df.to_dict( ))
    rows = []
    for index, row in df.iterrows():
        rows.append(  {'txn_time':index, 'token':row['token'],  'price':row['price'], 'total_volume': row['total_volume'], 'market_cap':row['market_cap']} )
    TokenHistoryPriceProcessor().save_price_to_db( rows )

def getProtocols():
    url = "https://api.llama.fi/protocols"
    r = requests.get(url)
    r_json = r.json()
    outfile = open("../data/gecko_all_protocols.json", 'w')
    json.dump( r_json , outfile )
    
    df = pd.DataFrame(r_json)
    df.set_index('name', inplace=True)

    ndf = df.loc[ df["address"].str.startswith("solana:", na=False) ]
    #print( ndf.shape )
    return ndf

def geckoMarkets(ticker):
    """Get top100 markets (pairs, quotes, exchanges, volume, spreads and more)
    
    Args:
        ticker (string): gecko ID, ie "bitcoin"
    
    Returns:
        DataFrame: Full detail markets available
    """
    url = f"https://api.coingecko.com/api/v3/coins/{ticker}/tickers"
    r = requests.get(url).json()['tickers']
    outfile = open("../data/sol_gecko_markets_" + ticker +".json", 'w')
    json.dump( r , outfile )

    df = pd.DataFrame(r)
    df['exchange'] = df['market'].apply(pd.Series)['name']
    df['volume_usd'] = df['converted_volume'].apply(pd.Series)['usd']
    df['price_usd'] = df['converted_last'].apply(pd.Series)['usd']

    df.set_index('exchange', inplace=True)
    cols = ['base','target','last', 'volume','bid_ask_spread_percentage','timestamp',
                   'volume_usd','price_usd','trust_score']
    df = df.loc[:,cols]
    cols[4] = 'spread'
    df.columns = cols
    df.timestamp = pd.to_datetime(df.timestamp)
    
    return df.sort_values('volume_usd', ascending=False)

def pcsPairInfo(base, quote):
    """get info from a token pair LP
    
    Args:
        base (string): Base LP token, ie "CAKE"
        quote (string): Quote LP token, ie "BNB"
        its the same if you call pcsPAirInfo('cake', 'bnb') or pcsPAirInfo('bnb', 'cake') 
    Returns:
        Dict: {
                 'pair_address': '0xA527a61703D82139F8a06Bc30097cC9CAA2df5A6',
                 'base_name': 'PancakeSwap Token',
                 'base_symbol': 'Cake',
                 'base_address': '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82',
                 'quote_name': 'Wrapped BNB',
                 'quote_symbol': 'WBNB',
                 'quote_address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c',
                 'price': '0.04311198194009326668',
                 'base_volume': '22248744.85',
                 'quote_volume': '934856.36',
                 'liquidity': '982769040.63',
                 'liquidity_BNB': '1878155.84'
                }
                * price is actually a ratio between base/quote tokens
    """
    url = "https://api.pancakeswap.info/api/v2/pairs"
    r = requests.get(url).json()
    data = r.get('data', None)
    print( r )
    res = f"Not found: {base}-{quote}"
    base = 'WBNB' if base.upper() == 'BNB' else base
    quote = 'WBNB' if quote.upper() == 'BNB' else quote
    
    for contract, values in data.items():
        base_ = base.upper() == values['base_symbol'].upper()
        quote_ = quote.upper() == values['quote_symbol'].upper()
        base_cross = base.upper() == values['quote_symbol'].upper()
        quote_cross = quote.upper() == values['base_symbol'].upper()

        if  (base_ and quote_) or  (base_cross and quote_cross):
            res = data[contract]
            break
            
    return res

#protocols_df =  getProtocols( ) 

#print( geckoHistorical( 'mSOL',  'marinade-staked-sol') )
#print( geckoHistorical( 'jito-staked-sol' ) )

#print( geckoHistorical( 'usd-coin' ) )
#print( geckoHistorical( 'tether' ) )
#print( geckoHistorical( 'RAY' , 'raydium' ) )
#print( geckoHistorical( 'SOL' , 'solana' ) )
#print( geckoHistorical( 'USDC', 'usd-coin' ) )
#print( geckoHistorical( 'USDT', 'tether' ) )


#print( geckoHistorical( 'lido-staked-sol'))
#print( geckoMarkets(  'frakt-token' ))
#print( pcsPairInfo ( 'cake', 'bnb' ))