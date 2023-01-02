from .databaseUtils import _create_list_of_stocks_table
from .databaseUtils import select_symbols
from .databaseUtils import insert_to_database

from .webscrapper import _get_hk_stocks_symbols_from_wikipedia

def get_symbols(market = "hk"):

    results = _create_list_of_stocks_table(market)
    df = select_symbols(market)

    if len(df) == 0:

        if market == "hk":
            df = _get_hk_stocks_symbols_from_wikipedia()
            results = insert_to_database(df, f"{market}_symbols")

        else:
            raise ValueError("Markets other than HK are not supported yet.")
  
    return df
