import sqlite3
import os

dirname = os.path.dirname(__file__)
print(dirname)
connection = sqlite3.connect(os.path.join(dirname, "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    """Palauttaa connection olion, jonka avulla tietokantaan ollaan yhteydessä."""

    return connection
