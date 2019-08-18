import json
import time
import ccxt
import asyncio
import ccxt.async_support as ccxt

#CCXT docs
#https://github.com/ccxt/ccxt/wiki/Manual#market-data
#https://github.com/ccxt/ccxt/wiki/Manual


#Configs
symbol = 'BTC/EUR'
delay = 2
###############################################################################################
kraken = ccxt.kraken() #Acess on kraken API
kraken.enableRateLimit = True #Turn on rate limiter to aviod ban
#print(dir(ccxt.kraken()))

allPairs =  kraken.load_markets()
symbolData = kraken.market(symbol)
allMarkets = kraken.fetch_markets() #returns an array of markets
symbols = kraken.symbols #All symbols of exchange
symbolId = kraken.market_id (symbol) # get market id by symbol
currencies = kraken.currencies   # a list of currencies

def getJSON(data):
    return (json.dumps(data, indent=4, sort_keys=True))


###############################################################################################
#Time conversion
kraken.parse8601 ('2018-01-01T00:00:00Z')# == 1514764800000 // integer, Z = UTC
kraken.iso8601 (1514764800000)# == '2018-01-01T00:00:00Z'   // iso8601 string
kraken.seconds ()# integer UTC timestamp in seconds
kraken.milliseconds ()# integer UTC timestamp in milliseconds


###############################################################################################
#CCXT functions
###############################################################################################
#Get orderbook
try:
    print( json.dumps(kraken.fetch_order_book (symbol)))
    time.sleep (delay) # rate limit
except Exception as e:
    print(e)

""""
#Example return
{
    'bids': [
        [ price, amount ], // [ float, float ]
        [ price, amount ],
        ...
    ],
    'asks': [
        [ price, amount ],
        [ price, amount ],
        ...
    ],
    'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
    'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
}
"""
###############################################################################################
#Market Depth

limit = 10
marketDepth = ccxt.cex().fetch_order_book(symbol, limit)
#return up to ten bidasks on each side of the order book stack

###############################################################################################

#Market Price
#current best price
orderbook = kraken.fetch_order_book (kraken.symbols[0])
bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
spread = (ask - bid) if (bid and ask) else None
print (kraken.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })


###############################################################################################
#Price Tickers

#Get all tickers from kranken
tickersAll = (kraken.fetch_tickers())

##########################################
#Get price ticker stattictics of a symbol
priceTickerSymbol = kraken.fetchTicker (symbol, params = {})

""""
{
    'symbol':        string symbol of the market ('BTC/USD', 'ETH/BTC', ...)
    'info':        { the original non-modified unparsed reply from exchange API },
    'timestamp':     int (64-bit Unix Timestamp in milliseconds since Epoch 1 Jan 1970)
    'datetime':      ISO8601 datetime string with milliseconds
    'high':          float, // highest price
    'low':           float, // lowest price
    'bid':           float, // current best bid (buy) price
    'bidVolume':     float, // current best bid (buy) amount (may be missing or undefined)
    'ask':           float, // current best ask (sell) price
    'askVolume':     float, // current best ask (sell) amount (may be missing or undefined)
    'vwap':          float, // volume weighed average price
    'open':          float, // opening price
    'close':         float, // price of last trade (closing price for current period)
    'last':          float, // same as `close`, duplicated for convenience
    'previousClose': float, // closing price for the previous period
    'change':        float, // absolute change, `last - open`
    'percentage':    float, // relative change, `(change/open) * 100`
    'average':       float, // average price, `(last + open) / 2`
    'baseVolume':    float, // volume of base currency traded for last 24 hours
    'quoteVolume':   float, // volume of quote currency traded for last 24 hours
}
"""
###############################################################################################
#Ticker(OHLC) of a symbol
tickerOfSymbol = (kraken.fetch_ticker(symbol))


time.sleep (kraken.rateLimit / 1000)
ohlcvSymbol = ((symbol, kraken.fetch_ohlcv (symbol, '1m')))

"""
#Example of return
[
        1504541580000, // UTC timestamp in milliseconds, integer
        4235.4,        // (O)pen price, float
        4240.6,        // (H)ighest price, float
        4230.0,        // (L)owest price, float
        4230.7,        // (C)losing price, float
        37.72941911    // (V)olume (in terms of the base currency), float
]

"""
###############################################################################################
# recent trades of a symbol
recentTrades = kraken.fetch_trades(symbol)

###############################################################################################
#asynchronous concurrency mode

async def print_kraken_symbol_ticker():
    poloniex = ccxt.kraken()
    print(await kraken.fetch_ticker(symbol))

asyncio.get_event_loop().run_until_complete(print_kraken_symbol_ticker())