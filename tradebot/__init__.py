"""
==========================================
TradeBot
Version: 0.0.1
Main Module
==========================================
Authors: Abhinav Vankayalapati
"""

import sys
from tradebot.broker.td_ameritrade import TDAmeritrade


class BollingerBot(object):
    def __init__(self, user, api_key, symbol):
        if symbol == '':
            print('must initialize class with user and api key')
            sys.exit(1)
        self.trade_platform = TDAmeritrade(user, api_key)
        self.symbol = symbol
        print('initializing bollinger bot for ' + symbol)

    def initialize(self):
        self.trade_platform.authenticate()
        self.trade_platform.get_price(self.symbol)
