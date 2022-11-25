from database_connection import get_database_connection
import os

def create_table(connection):
    connection.execute("CREATE TABLE Questions (id INTEGER PRIMARY KEY, Question TEXT)")
    


def remove_database():
    if os.path.exists("testi.db"):
        os.remove("testi.db")
    

def init_database():
    remove_database()
    connection = get_database_connection()
    create_table(connection)
    return connection
