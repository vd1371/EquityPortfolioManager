from ._make_query import make_query

def _create_list_of_stocks_table(market = "hk"):

    command = f"""
        CREATE TABLE {market}_symbols (
            code CHAR(4) PRIMARY KEY,
            name TEXT
        )"""

    res = make_query(command)

    if res['message'] == None:
        raise ValueError(res['message'])

    return res