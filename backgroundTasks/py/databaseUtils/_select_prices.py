import pandas as pd

from ._make_query import make_query
from py.utils.template_names import table_name, price_columns

def select_prices(stock, frequency):

    command = f"SELECT * from {table_name(stock, frequency)}"
    res = make_query(command)

    df = pd.DataFrame(res['results'], columns = price_columns)
    df.set_index("date", drop = True, inplace = True)

    return df