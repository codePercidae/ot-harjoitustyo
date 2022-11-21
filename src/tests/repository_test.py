import unittest
from question_repository import QuestionRepository

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repositry = QuestionRepository()

    def test_add_question_adds_new_question_to_dictionary(self):
        self.repositry.add_question("New question")
        self.assertEqual(self.repositry.questions["New question"], [])
