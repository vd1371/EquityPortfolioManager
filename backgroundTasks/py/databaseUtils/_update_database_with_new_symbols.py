from ._insert_to_database import insert_to_database
from ._select_symbols import select_symbols

def _update_database_with_new_symbols(df, market = "hk"):

    results = {
        "results" : None,
        "message" : "Already Updated"
    }
    available_df = select_symbols(market)
    df_for_insertion = df.copy().drop(index = available_df.index, errors = "ignore")

    if len(df_for_insertion) > 0:
        results["results"] = insert_to_database(
            df_for_insertion, f"{market}_symbols"
        )
        results["message"] = "Interacted with the database"

    return results