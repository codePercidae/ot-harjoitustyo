from question_repository import QuestionRepository
from interface import Interface
from grade_interface import GradeInterface


class DailyQuestionsApp:

    def __init__(self) -> None:
        self.repository = QuestionRepository()
        self.main_gui = Interface(self)

    def start_gui(self):
        self.main_gui.activate()

    def new_question(self, question):
        if len(question) == 0:
            return False
        else:
            return self.repository.add_question(question)
    
    def grade_window(self):
        self.main_gui.kill()
        self.grade_gui = GradeInterface(self)
        self.grade_gui.activate()

    def transmit_questions(self):
        return self.repository.get_questions()

    def grade_question(self, question_id, grade):
        if grade in [str(i) for i in range(1, 11)]:
            self.repository.new_grade(question_id, grade)
            return True
        else:
            return False

    def kill_grade_gui(self):
        self.grade_gui.kill()
        self.main_gui.activate()

    def empty_database(self):
        self.repository.initialize_database()
