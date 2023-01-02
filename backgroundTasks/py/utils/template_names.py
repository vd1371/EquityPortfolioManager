price_columns = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']

def table_name(stock, frequency):
    return f"HK_{stock}_{frequency}"