from datetime import date
from initialize_database import init_database

class QuestionRepository:
    def __init__(self) -> None:
        self.connection = init_database()

    def add_question_db(self, question):
        self.connection.execute(f"INSERT INTO Questions (question) VALUES ('{question}')")
        question_id = self.connection.execute(f"SELECT * FROM Questions WHERE question='{question}").fetchone()[0]
        self.connection.execute(f"CREATE TABLE Question_{question_id} (id INTEGER PRIMARY KEY, date DATE, grade INTEGER)")

    def get_questions_db(self):
        return self.connection.execute("SELECT * FROM Questions").fetchall()
            
    def new_grade_db(self, question, grade):
        self.connection.execute(f"INSERT INTO {question} (date, grade) VALUES ({date.today()}, {grade})")
