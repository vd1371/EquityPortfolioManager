from py import _find_symbols_of_hong_kong_stocks
from py import _get_historical_data_of_stock


def run():
    # _find_symbols_of_hong_kong_stocks()

    code = "0002"

    df = _get_historical_data_of_stock(code)

    _update_database_with_(code, df)


if __name__ == "__main__":
    run()