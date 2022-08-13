"""
==========================================
TradeBot
Version: 0.0.1
TD Ameritrade Module
==========================================
Authors: Abhinav Vankayalapati
"""
import sys
import requests
import json

class TDAmeritrade(object):
    # write initialize function
    def __init__(self, user, api_key):
        if user == '' or api_key == '':
            print('must initialize class with user and api key')
            sys.exit(1)
        self.user = user
        self.api_key = api_key

    def authenticate(self):
        print(self.user)
        print(self.api_key)

    def get_price(self, symbol):
        endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'
        full_url = endpoint.format(stock_ticker=symbol)
        page = requests.get(url=full_url,
                            params={'apikey': self.api_key})
        content = json.loads(page.content)
        print(content)