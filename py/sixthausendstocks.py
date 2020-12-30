import requests
import json
import datetime

url = 'https://financialmodelingprep.com/api/v3/stock/list?apikey=c1d5db3bf65299abe6068e556f5bed6e'

response = requests.get(url)
allist = json.loads(response.text)

print('Done, count:', len(allist))

with open('20k_worldwide_stockList.json', 'w') as f:
    json.dump(allist, f)
 
print('1/3 done')
# "exchange": "New York Stock Exchange" -2625
# "exchange": "Nasdaq" - 1539
# "exchange": "Nasdaq Global Select" -1505

# Batch requests
# https://financialmodelingprep.com/api/v3/quote/AAPL,FB,GOOG?apikey=c1d5db3bf65299abe6068e556f5bed6e
batch_url = 'https://financialmodelingprep.com/api/v3/quote/'
api_key   = 'apikey=c1d5db3bf65299abe6068e556f5bed6e'
batchList =  ''

for stock in allist:
    if 'exchange' in stock:
        if (str(stock['exchange']) == 'New York Stock Exchange' ) or (str(stock['exchange']) == 'Nasdaq' ) or (str(stock['exchange']) == 'Nasdaq Global Select' ) :
            batchList = batchList + stock['symbol'] + ','
        
batchList = batchList[0:len(batchList)-1]
batch_url = batch_url + batchList + '?' + api_key

batchResponse = requests.get(batch_url)

print(batch_url)
#fulllist = json.loads(batchResponse.text)

# print('2/3 done')

# for result in fulllist:
    # result["timestamp"] = datetime.datetime.fromtimestamp( result["timestamp"] ).strftime('%Y-%m-%d %H:%M:%S')

# with open('6000_fulllist.json', 'w') as f:
    # json.dump(fulllist, f)

# print('3/3 done')