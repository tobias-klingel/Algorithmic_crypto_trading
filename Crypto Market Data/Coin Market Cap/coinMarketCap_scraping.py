import pandas as pd
import datetime

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import coinMarketCap_parameters as param

#https://pro.coinmarketcap.com/account
#https://coinmarketcap.com/api/documentation/v1/#
################################################################################
#Cryptocurrency
url_map = "map" #Get CoinMarketCap ID map
url_info= "info" # Get metadata
url_listings_latest = "listings/latest" #List all cryptocurrencies (latest)
url_listings_historical = "listings/historical" #List all cryptocurrencies (historical)
url_quotes_latest = "quotes/latest" #Get market quotes (latest)
url_quotes_historical = "quotes/historical" #Get market quotes (historical)
url_market_pairs_latest = "market-pairs/latest" #Get market pairs (latest)
url_ohlcv_latest = "ohlcv/latest" #Get OHLCV values (latest)
url_ohlcv_historical = "ohlcv/historical" #Get OHLCV values (historical)
################################################################################
#Exchange
#Same as Cryptocurrency
################################################################################
#Global-Metrics
url_quotes_latest = "quotes/latest" #Get aggregate market metrics (latest)
url_quotes_historical = "quotes/historical" #Get aggregate market metrics (historical)

################################################################################
#Tools
url = "price-conversion" #Convert an amount of one cryptocurrency into other currencies
                         # using current or historical rates
################################################################################
#Endpoint urls
url_endPoint_cryptocurrency = "cryptocurrency/"
url_endPoint_exchange = "exchange/"
url_endPoint_global_metrics= "global-metrics/"
url_endPoint_tools = "tools/"

##################################################
#Core API url
url_core = "https://pro-api.coinmarketcap.com/v1/"
##################################################

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '!!!!!!!!!!!!!!!INPUT_THE_API_KEY!!!!!!!!!!!!!!!!!!!!!!',
}
##################################################
session = Session()
session.headers.update(headers)

##################################################
#ToDo
#----------------------------> #Need to be adjusted <----------------------------
#Url creation (this url will be used to call API)
url_to_call = url_core + url_endPoint_cryptocurrency +url_map
urlParameter = param.parameters_cryptocurrency_map
#----------------------------> #Need to be adjusted <----------------------------
##################################################
try:
    response = session.get(url_to_call, params = urlParameter)
    data = json.loads(response.text)
    print(json.dumps(data, sort_keys=True, indent=4))
    #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
