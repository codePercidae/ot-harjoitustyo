from question_repository import QuestionRepository
from interface import Interface

GUIDE = """To save a new daily question, input n\n
To grade your daily questions, input g\n
To see the previus answers, input s\n
To remove all entries, input FORMAT\n
To exit input, x\n"""


class DailyQuestionsApp:

    def __init__(self) -> None:
        self.repository = QuestionRepository()
        self.gui = Interface(self)

    def start_gui(self):
        self.gui.activate()

    def new_question(self, question):
        return self.repository.add_question(question)
    
    def transmit_questions(self):
        return self.repository.get_questions()

    def grade_question(self, question, grade):
        self.repository.new_grade(question, grade)

    def show_answers(self):
        questions = self.repository.get_questions()
        for question in questions:
            values = self.repository.get_values(question[0])
            print(question[1])
            print(str(values) + "\n")

    def empty_database(self):
        self.repository.initialize_database()