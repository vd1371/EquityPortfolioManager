from ._make_query import make_query
from py.utils.template_names import table_name

def _create_price_table(stock, frequency):

    command = f"""
        CREATE TABLE {table_name(stock, frequency)} (
            date DATE PRIMARY KEY,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            adj_close REAL,
            volume REAL
        )"""

    res = make_query(command)

    if res['message'] == None:
        raise ValueError(res['message'])

    return res