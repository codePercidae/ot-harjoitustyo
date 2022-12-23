import sqlite3
import os
from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)
print(dirname)
connection = sqlite3.connect(os.path.join(DATABASE_FILE_PATH))
connection.row_factory = sqlite3.Row


def get_database_connection():
    """Palauttaa connection olion, jonka avulla tietokantaan ollaan yhteydessä."""

    return connection
