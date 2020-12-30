import requests
import json
import datetime

url = 'https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=c1d5db3bf65299abe6068e556f5bed6e'

resp = requests.get(url=url)
list_stocks = resp.json() # Check the JSON Response Content documentation below

print('Done, count:', len(list_stocks))

with open('list_stocks.json', 'w') as f:
    json.dump(list_stocks, f)
    
    
    
#Batch requests
#https://financialmodelingprep.com/api/v3/quote/AAPL,FB,GOOG?apikey=c1d5db3bf65299abe6068e556f5bed6e
batch_url = 'https://financialmodelingprep.com/api/v3/quote/'
api_key   = 'apikey=c1d5db3bf65299abe6068e556f5bed6e'
batchList =  ''

for stock in list_stocks:
    batchList = batchList + stock['symbol'] + ','

batchList = batchList[0:len(batchList)-1]

batch_url = batch_url + batchList + '?' + api_key

batchResponse = requests.get(batch_url).json()

for result in batchResponse:
    result["timestamp"] = datetime.datetime.fromtimestamp( result["timestamp"] ).strftime('%Y-%m-%d %H:%M:%S')

with open('batchResponse.json', 'w') as f:
    json.dump(batchResponse, f)