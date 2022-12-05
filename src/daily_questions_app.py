from question_repository import QuestionRepository
from interface import Interface


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
