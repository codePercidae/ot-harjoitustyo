from datetime import date
from sqlite3 import OperationalError
from database_connection import get_database_connection
from initialize_database import init_database


class QuestionRepository:

    def __init__(self) -> None:
        self.connection = get_database_connection()

    # New questions create new tables where grades are stored.
    # Tables are named in form Question_id where
    # id represents the id number given by the Questions table.
    # Horrible way to implement this, too bad.

    def add_question(self, question):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"INSERT INTO Questions (question) VALUES ('{question}')")
            self.connection.commit()
            question_id = cursor.execute(
                f"SELECT * FROM Questions WHERE question='{question}'").fetchone()[0]
            cursor.execute(
                f"""CREATE TABLE Question_{question_id}
                (id INTEGER PRIMARY KEY, date DATE, grade INTEGER)""")
            self.connection.commit()
            return True
        except OperationalError:
            return False

    # returns all the contents from Questions table

    def get_questions(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions")
        rows = cursor.fetchall()
        return [(row["id"], row["question"]) for row in rows]

    def new_grade(self, question_id, grade):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Question_{question_id} (date, grade) VALUES ({date.today()}, {grade})")
        self.connection.commit()

    def get_values(self, question_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM Question_{question_id}")
        rows = cursor.fetchmany(5)
        return [row["grade"] for row in rows]

    def initialize_database(self):
        init_database()
