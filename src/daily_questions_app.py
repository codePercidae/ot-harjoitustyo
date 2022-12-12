from question_repository import QuestionRepository
from ui.grade_interface import GradeInterface
from ui.interface import Interface
from ui.status_interface import StatusInterface

class DailyQuestionsApp:

    def __init__(self) -> None:
        self.repository = QuestionRepository()

    def start_gui(self):
        self.main_gui = Interface(self)
        self.main_gui.activate()

    def new_question(self, question):
        if len(question) == 0:
            return False
        return self.repository.add_question(question)

    def grade_window(self):
        self.main_gui.kill()
        self.grade_gui = GradeInterface(self)
        self.grade_gui.activate()

    def transmit_questions(self):
        return self.repository.get_questions()

    def transmit_answers(self, question_id):
        return self.repository.get_values(question_id)

    def grade_question(self, question_id, grade):
        if grade in [str(i) for i in range(1, 11)]:
            self.repository.new_grade(question_id, grade)
            return True
        return False

    def archive(self, question_id):
        self.repository.deactive(question_id)

    def status_window(self):
        self.main_gui.kill()
        self.status_gui = StatusInterface(self)

    def kill_status_gui(self):
        self.status_gui.kill()
        self.start_gui()

    def kill_grade_gui(self):
        self.grade_gui.kill()
        self.start_gui()

    def empty_database(self):
        self.repository.initialize_database()
