import sqlite3
import os

connection = sqlite3.connect("testi.db")
connection.isolation_level = None


def get_database_connection():
    if os.path.exists("testi.db"):
        print("connect")    
    return connection