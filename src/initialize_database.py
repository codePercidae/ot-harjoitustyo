from database_connection import get_database_connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, Question TEXT, Active BOOL)")
    connection.commit()

def remove_database(connection):
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
    connection = get_database_connection()
    remove_database(connection)
    create_table(connection)

if __name__ == "__main__":
    init_database()
