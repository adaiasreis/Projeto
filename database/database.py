import sqlite3

URL_DATABASE = 'database/db_loccar.db'

def connect_db():
    conn = sqlite3.connect(URL_DATABASE)
    return conn