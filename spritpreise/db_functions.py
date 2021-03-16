from pathlib import Path
import sqlite3
import pandas as pd
#from sqlite3.dbapi2 import DatabaseError


BASE_DIR = Path(__file__).resolve().parent


def get_fields():
    return ("id", "name", "brand", "street", "place", "lat", "lng", "dist", "diesel", "e5", "e10", "isOpen",
            "houseNumber", "postCode", "datetime")


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)

    return conn


def add_to_db(id, name, brand, street, place, lat, lng, dist,
              diesel, e5, e10, isOpen, houseNumber, postCode, dt) -> None:
    connection = create_connection("spritpreise.db")
    cur = connection.cursor()
    fields = get_fields()
    sql = f"INSERT INTO daten {fields} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    sql = sql.replace("\n", "")
    sql = sql.replace("\\", "")
    cur.execute(sql, (id, name, brand, street, place, lat, lng, dist,
                      diesel, e5, e10, isOpen, houseNumber, postCode, dt
                      )
                )
    connection.commit()
    connection.close()


def read_from_db(sql: str) -> list:
    result = []
    connection = create_connection("spritpreise.db")
    cur = connection.cursor()
    #try:
    cur.execute(sql)
    result = cur.fetchall()
    connection.close()
    return result
    #except DatabaseError as e:
    
    #print(f"Fehler: Daten können nicht aus Datenbank gelesen werden. {e}")
    #return result


def get_from_db(db_name):
    con = sqlite3.connect(db_name)
    df = pd.read_sql("SELECT * FROM daten", con)
    return df
