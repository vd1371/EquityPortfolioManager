import pandas as pd

from ._make_query import make_query
from py.utils.template_names import table_name

def select_symbols(market = "hk"):

    command = f"SELECT * from {market}_symbols"
    res = make_query(command)

    df = pd.DataFrame(res['results'], columns = ["code", "name"])
    df.set_index("code", drop = True, inplace = True)

    return df