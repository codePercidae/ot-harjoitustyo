from datetime import date
from database_connection import get_database_connection

class QuestionRepository:
    def __init__(self) -> None:
        self.connection = get_database_connection()

    def add_question_db(self, question):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Questions (question) VALUES ('{question}')")
        self.connection.commit()
        question_id = cursor.execute(f"SELECT * FROM Questions WHERE question='{question}'").fetchone()[0]
        cursor.execute(f"CREATE TABLE Question_{question_id} (id INTEGER PRIMARY KEY, date DATE, grade INTEGER)")
        self.connection.commit()

    def get_questions_db(self):
        cursor = self.connection.cursor()
        return cursor.execute("SELECT * FROM Questions").fetchall()
            
    def new_grade_db(self, question, grade):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO {question} (date, grade) VALUES ({date.today()}, {grade})")
        self.connection.commit()
