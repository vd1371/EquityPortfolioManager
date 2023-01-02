import os
import psycopg2

def make_query(query, data = None):

    conn = None
    results, message = None, None
    try:
        params = {
            "database" : os.getenv("DATABASE_NAME"),
            "user" : os.getenv("DATABASE_USER"),
            "password" : os.getenv("DATABASE_PASSWORD"),
            "host" : os.getenv("DATABASE_HOST"),
            "port" : os.getenv("DATABASE_PORT")
        }
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if "INSERT" in query:
            cur.executemany(query, data)
        else:
            cur.execute(query)
        
        if "select" in query.lower():
            results = cur.fetchall()
        
        cur.close()
        conn.commit()
        message = "Successful"

    except (Exception, psycopg2.DatabaseError) as error:
        message = error.__str__()

    finally:
        if conn is not None:
            conn.close()

    return {
        "results": results,
        "message": message
    }