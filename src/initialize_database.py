from sqlite3 import *

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, Question TEXT)")
    connection.commit()


def remove_database(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    if cursor.fetchall():
        cursor.execute("SELECT * FROM Questions")
        rows = cursor.fetchall()
        for id in [row["id"] for row in rows]:
            cursor.execute(f"DROP TABLE IF EXISTS Question_{id}")
        cursor.execute("DROP TABLE Questions")
        connection.commit()
        

def init_database(connection):
    remove_database(connection)
    create_table(connection)
    
