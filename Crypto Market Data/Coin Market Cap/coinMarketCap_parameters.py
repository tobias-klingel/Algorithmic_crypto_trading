##################################################
#Parameter
#Get CoinMarketCap ID map
#/v1/cryptocurrency/map
parameters_cryptocurrency_map = {
  'listing_status':'active', #Only active cryptocurrencies ->Default is active
  'start':'1', #>= 1
  'limit':'5000', #[ 1 .. 5000 ]
  'symbol':'BTC,USDT,BNB',
   'aux': 'platform' #platform,first_historical_data,last_historical_data,is_active,status
}
##############################
#Get cryptocurrency metadata
#/v1/cryptocurrency/info
parameters_metadata = {
  'id':'1',
  'slug':'1', #comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
  'symbol':'BTC' # Example: "BTC,ETH"
}
##############################
#List all cryptocurrencies (latest)
# /v1/cryptocurrency/listings/latest
parameters_latest = {
  'start':'1',#>= 1
  'limit':'1', #[ 1 .. 5000 ]
  'convert':'USD',# https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
  'convert_id':'1,2781', # identical to convert convert_id=1,2781 ->convert=BTC,USD
  'sort':'1', #"cmc_rank" "name" "symbol" "date_added" "market_cap" "price" "circulating_supply" "total_supply" "max_supply" "volume_24h" "percent_change_1h" "percent_change_24h" "percent_change_7d"
  'sort_dir':'asc', #"asc" "desc"
  'cytrocurrency_type':'all', #"all" "coins" "tokens"
  'aux':'num_market_pairs' #num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
}
##############################
#List all cryptocurrencies (historical)
#/v1/cryptocurrency/listings/historical
parameters_cryptocurrencies_historical = {
    'date': '2018-01-02', #date (Unix or ISO 8601)
    'start': '1',  # >= 1
    'limit': '1',  # [ 1 .. 5000 ]
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781',  # identical to convert convert_id=1,2781 ->convert=BTC,USD
    'sort': '1',# "cmc_rank" "name" "symbol" "date_added" "market_cap" "price" "circulating_supply" "total_supply" "max_supply" "volume_24h" "percent_change_1h" "percent_change_24h" "percent_change_7d"
    'sort_dir': 'asc',  # "asc" "desc"
    'cytrocurrency_type': 'all',  # "all" "coins" "tokens"
}
##############################
#Get market quotes (latest)
#/v1/cryptocurrency/quotes/latest
parameters_latest = {
  'id':'1', #date (Unix or ISO 8601) #'2018-01-01'
  'slug':'1', #comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
  'symbol':'BTC', # Example: "BTC,ETH"
  'convert':'USD',# https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
  'convert_id':'1,2781', # identical to convert convert_id=1,2781 ->convert=BTC,USD
  'aux':'num_market_pairs' #num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
}
##############################
#Get market quotes (historical)
#/v1/cryptocurrency/quotes/historical
parameters_quotes_historical = {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'symbol': 'BTC',  # Example: "BTC,ETH"
    'time_start': '1',  #Timestamp (Unix or ISO 8601)
    'time_end': '2018-06-22T19:35:00',  #Timestamp (Unix or ISO 8601)
    'count': '1,2781',  #[ 1 .. 10000 ], default 10,number of interval periods
    'interval': '1',#"yearly" "monthly" "weekly" "daily" "hourly" "5m" "10m" "15m" "30m" "45m" "1h" "2h" "3h" "6h" "12h" "24h" "1d" "2d" "3d" "7d" "14d" "15d" "30d" "60d" "90d" "365d"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}

##############################
#Get market pairs (latest)
#/v1/cryptocurrency/market-pairs/latest
parameters_pairs_latest= {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'slug': '1',  # comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
    'start': '1',  # >= 1
    'limit': '1',  # [ 1 .. 5000 ]
    'aux': 'num_market_pairs',  # num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
#Get OHLCV values (latest)
#/v1/cryptocurrency/ohlcv/latest
parameters_OHLCV_latest = {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'symbol': 'BTC',  # Example: "BTC,ETH"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}

##############################
#Get OHLCV values (historical)
#/v1/cryptocurrency/ohlcv/historical
parameters_OHLCV_historical = {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'slug': '1',  # comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
    'symbol': 'BTC',  # Example: "BTC,ETH"
    'time_period': 'daily',  # "daily" "hourly"
    'time_start': '1',  # Timestamp (Unix or ISO 8601)
    'time_end': '2018-06-22T19:35:00',  # Timestamp (Unix or ISO 8601)
    'count': '1,2781',  # [ 1 .. 10000 ], default 10,number of interval periods
    'interval': '1',# "yearly" "monthly" "weekly" "daily" "hourly" "5m" "10m" "15m" "30m" "45m" "1h" "2h" "3h" "6h" "12h" "24h" "1d" "2d" "3d" "7d" "14d" "15d" "30d" "60d" "90d" "365d"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################

##############################
#Get CoinMarketCap ID map
#/v1/exchange/map
parameters_exchange_map = {
  'listing_status':'active', #Only active cryptocurrencies ->Default is active
  'slug':'1', #comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
  'start': '1',  # >= 1
  'limit': '1',  # [ 1 .. 5000 ]
  'aux': 'num_market_pairs', # num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
}
##############################
#Get exchange metadata
#/v1/exchange/info
parameters_exchange_info = {
  'id':'1',
  'slug':'1' #comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
}
##############################
#List all exchanges (latest)
# /v1/exchange/listings/latest
parameters_exchanges_latest = {
  'start':'1',#>= 1
  'limit':'1', #[ 1 .. 5000 ]
  'sort': '1',# "cmc_rank" "name" "symbol" "date_added" "market_cap" "price" "circulating_supply" "total_supply" "max_supply" "volume_24h" "percent_change_1h" "percent_change_24h" "percent_change_7d"
  'sort_dir': 'asc',  # "asc" "desc"
  'market_type':'all', #"fees" "no_fees" "all"
  'aux':'num_market_pairs', #num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
  'convert':'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
  'convert_id': '1,2781',  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
#List all exchanges (historical)
# /v1/exchange/listings/historical
parameters_exchanges_listings_historical = {
  'timestamp': '2019-07-01T18:15:15.788Z',  #Timestamp (Unix or ISO 8601)
  'start':'1',#>= 1
  'limit':'1', #[ 1 .. 5000 ]
  'sort': '1',# "cmc_rank" "name" "symbol" "date_added" "market_cap" "price" "circulating_supply" "total_supply" "max_supply" "volume_24h" "percent_change_1h" "percent_change_24h" "percent_change_7d"
  'sort_dir': 'asc',  # "asc" "desc"
  'market_type':'all', #"fees" "no_fees" "all"
  'convert':'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
}
##############################
#Get market quotes (latest)
#/v1/exchange/quotes/latest
parameters_exchange_quotes_latest = {
    'id': '1',  # date (Unx or ISO 8601) #'2018-01-01'
    'slug': '1',  # comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
#Get market quotes (historical)
#/v1/exchange/quotes/historical
parameters_exchange_quotes_historical = {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'slug': '1',  # comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
    'time_start': '1',  # Timestamp (Unix or ISO 8601)
    'time_end': '2018-06-22T19:35:00',  # Timestamp (Unix or ISO 8601)
    'count': '1,2781',  # [ 1 .. 10000 ], default 10,number of interval periods
    'interval': '1',# "yearly" "monthly" "weekly" "daily" "hourly" "5m" "10m" "15m" "30m" "45m" "1h" "2h" "3h" "6h" "12h" "24h" "1d" "2d" "3d" "7d" "14d" "15d" "30d" "60d" "90d" "365d"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
#List all market pairs (latest)
#/v1/exchange/market-pairs/latest
parameters_exchange_market_pairs_latest = {
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'slug': '1',  # comma-separated list of cryptocurrency slugs. Example: "bitcoin,ethereum"
    'start': '1',  # >= 1
    'limit': '1',  # [ 1 .. 5000 ]
    'aux': 'num_market_pairs',# num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################

##############################
#Global-Metrics
#/v1/global-metrics/quotes/latest
parameters_global_metrics_quotes_latest = {
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
#Get aggregate market metrics (historical)
#/v1/global-metrics/quotes/historical
parameters_global_metrics_quotes_historical = {
    'time_start': '1',  # Timestamp (Unix or ISO 8601)
    'time_end': '2018-06-22T19:35:00',  # Timestamp (Unix or ISO 8601)
    'count': '1,2781',  # [ 1 .. 10000 ], default 10,number of interval periods
    'interval': '1',# "yearly" "monthly" "weekly" "daily" "hourly" "5m" "10m" "15m" "30m" "45m" "1h" "2h" "3h" "6h" "12h" "24h" "1d" "2d" "3d" "7d" "14d" "15d" "30d" "60d" "90d" "365d"
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}

##################################################################################################################################################################################################################
##################################################################################################################################################################################################################

##############################
#Tools
#/v1/tools/price-conversion
parameters_tools_price_conversion = {
    'amount': '1',  #[ 1e-8 .. 1000000000 ],  Example: 10.43
    'id': '1',  # date (Unix or ISO 8601) #'2018-01-01'
    'symbol': 'BTC',  # Example: "BTC,ETH"
    'time': '2018-06-22T19:35:00',  # Timestamp (Unix or ISO 8601), reference historical pricing during conversion.
    'convert': 'USD',  # https://coinmarketcap.com/api/documentation/v1/#section/Standards-and-Conventions
    'convert_id': '1,2781'  # identical to convert convert_id=1,2781 ->convert=BTC,USD
}
##############################
