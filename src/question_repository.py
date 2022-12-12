from datetime import date
from sqlite3 import OperationalError
from database_connection import get_database_connection
from initialize_database import init_database


class QuestionRepository:

    def __init__(self) -> None:
        self.connection = get_database_connection()

    def add_question(self, question):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"INSERT INTO Questions (question, active) VALUES ('{question}', TRUE)")
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

    def get_questions(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions where active=TRUE")
        rows = cursor.fetchall()
        return [(row["id"], row["question"]) for row in rows]

    def deactive(self, question_id):
        cursor = self.connection.cursor()
        cursor.execute(f"UPDATE Questions SET active=FALSE WHERE id = {question_id}")
        self.connection.commit()

    def new_grade(self, question_id, grade):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Question_{question_id} (date, grade) VALUES ({date.today()}, {grade})")
        self.connection.commit()

    def get_values(self, question_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM Question_{question_id}")
        rows = cursor.fetchmany(7)
        return [row["grade"] for row in rows]

    def initialize_database(self):
        init_database()
