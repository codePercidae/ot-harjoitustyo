from database_connection import get_database_connection

def _create_table(connection):
    """Luo Questions taulun tietokantaan jolla on rivit
        id: kysymyksen yksilöllinen tunniste
        Question: itse kysymys
        Active: kertoo onko kysymys aktiivinen vai arkistoitu
    """

    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, Question TEXT, Active BOOL)")
    connection.commit()

def _remove_database(connection):
    """Poistaa kaikki taulut tietokannasta"""

    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    if cursor.fetchall():
        cursor.execute("SELECT * FROM Questions")
        rows = cursor.fetchall()
        for question_id in [row["id"] for row in rows]:
            cursor.execute(f"DROP TABLE IF EXISTS Question_{question_id}")
        cursor.execute("DROP TABLE Questions")
        connection.commit()

def init_database():
    """Tyhjentää tietokannan ja alustaa sen"""

    connection = get_database_connection()
    _remove_database(connection)
    _create_table(connection)


if __name__ == "__main__":
    init_database()
