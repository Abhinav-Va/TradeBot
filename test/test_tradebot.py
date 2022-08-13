"""
==========================================
TradeBot
Version: 0.0.1
Test Module
==========================================
Authors: Abhinav Vankayalapati
"""
import os
from decouple import config
from tradebot import BollingerBot
from unittest import main as test_main, SkipTest, TestCase


def test_broker_connection():
    API_USERNAME = config('USER')
    API_KEY = config('API_KEY')
    test_tradebot = BollingerBot(API_USERNAME, API_KEY, 'GOOG')
    test_tradebot.initialize()


if __name__ == "__main__":
    test_broker_connection()
