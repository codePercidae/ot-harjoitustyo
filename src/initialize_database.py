from database_connection import get_database_connection
import os

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, Question TEXT)")
    connection.commit()


def remove_database(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    if cursor.fetchall():
        tables = cursor.execute("SELECT * FROM Questions").fetchall()
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[1]}")
        cursor.execute("DROP TABLE Questions")
        connection.commit()
        

def init_database():
    connection = get_database_connection()
    remove_database(connection)
    create_table(connection)
    
