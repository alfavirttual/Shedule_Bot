import psycopg2
from config import host, user, password, db_name, port

try:
    # connect to exist database
    connection = psycopg2.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            firs_name varchar(50) NOT NULL);"""
        )

    print("[INFO] Table created successfully")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
