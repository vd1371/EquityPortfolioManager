from ._make_query import make_query

def insert_to_database(df, table):

    df_for_insertion = df.copy()
    df_for_insertion.reset_index(inplace = True)

    tuples = [tuple(x) for x in df_for_insertion.to_numpy()]
    cols = ', '.join(list(df_for_insertion.columns)).lower()
    vals_holder = ", ".join(["%s" for _ in df_for_insertion.columns])
    
    command = f"INSERT INTO {table} ({cols}) VALUES ({vals_holder})"
    results = make_query(command, data = tuples)

    return results
    