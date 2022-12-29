import os
import psycopg2

def _create_table(stock, frequency):
    """ create tables in the PostgreSQL database"""
    commands = (
        f"""
        CREATE TABLE HK_{stock}_{frequency} (
            date DATE PRIMARY KEY,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            adj_close REAL,
            volume REAL
        )
        """,
    )

    conn = None
    try:
        # read the connection parameters
        params = {
            "database" : os.getenv("DATABASE_NAME"),
            "user" : os.getenv("DATABASE_USER"),
            "password" : os.getenv("DATABASE_PASSWORD"),
            "host" : os.getenv("DATABASE_HOST"),
            "port" : os.getenv("DATABASE_PORT")
        }
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if "already exists" in error:
            pass
        else:
            print(error)
    finally:
        if conn is not None:
            conn.close()