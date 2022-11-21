#This class will implement the database for the application. Currently no permanent storage of data.

class QuestionRepository:
    def __init__(self) -> None:
        self.questions = {}

#Active test
    def add_question(self, question):
        self.questions[question]=[]

#No test
    def get_questions(self):
        return self.questions
    
#No test
    def new_grade(self, question, grade):
        self.questions[question].append(grade)