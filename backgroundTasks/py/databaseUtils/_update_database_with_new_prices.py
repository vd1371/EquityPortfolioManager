from ._insert_to_database import insert_to_database
from ._select_prices import select_prices

from py.utils.template_names import table_name

def _update_database_with_new_prices(df, stock, frequency):

    results = {
        "results" : None,
        "message" : "Already Updated"
    }
    available_df = select_prices(stock, frequency)
    df_for_insertion = df.copy().drop(index = available_df.index, errors = "ignore")

    if len(df_for_insertion) > 0:
        table = table_name(stock, frequency)
        results["results"] = insert_to_database(
            df_for_insertion, table
        )
        results["message"] = "Interacted with the database"

    return results