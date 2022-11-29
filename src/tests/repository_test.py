import unittest
from question_repository import QuestionRepository


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = QuestionRepository()
        self.repository.initialize_database()

    def test_add_question_adds_new_question_to_database(self):
        self.repository.add_question("New question")
        self.assertEqual(self.repository.get_questions()[0][1], "New question")

    def test_new_grade_sets_correct_grade(self):
        self.repository.add_question("New question")
        self.repository.new_grade(1, 5)
        self.assertEqual(self.repository.get_values(1)[0], 5)
