import unittest
from daily_questions_app import DailyQuestionsApp
from initialize_database import init_database


class Testapp(unittest.TestCase):
    def setUp(self):
        init_database()
        self.app = DailyQuestionsApp()

    def test_zero_length_question_not_accepted(self):
        self.assertEqual(self.app.new_question(""), False)

    def test_unvalid_grade_return_false(self):
        self.app.new_question("New question")
        self.assertEqual(self.app.grade_question("1", "0"), False)

    def test_valid_grade_return_true(self):
        self.app.new_question("New question")
        self.assertEqual(self.app.grade_question("1", "1"), True)

