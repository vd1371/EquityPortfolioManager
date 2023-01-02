import pandas as pd
from datetime import datetime

from .databaseUtils import _create_list_of_stocks_table
from .databaseUtils import _create_price_table
from .databaseUtils import _update_database_with_new_prices

from .webscrapper import _get_historical_data_of_stock
from .get_symbols import get_symbols

from .utils import logger

def start_database_updating_engine():

    logger.info("Hello")

    while True:
        if datetime.now().hour == 19:

            market = "hk"
            results = _create_list_of_stocks_table(market)
            df_symbols = get_symbols(market).iloc[:15]

            for stock_code, stock_name in zip(
                df_symbols['code'],
                df_symbols['name']
            ):
                _create_price_table(stock = stock_code, frequency="1d")
                df_prices = _get_historical_data_of_stock(stock_code)
                result = _update_database_with_new_prices(
                    df_prices,
                    stock_code, "1d"
                )