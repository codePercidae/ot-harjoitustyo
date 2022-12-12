import unittest
from question_repository import QuestionRepository


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = QuestionRepository()
        self.repository.initialize_database()
        self.repository.add_question("New question")

    def test_add_question_adds_new_question_to_database(self):
        self.assertEqual(self.repository.get_questions()[0][1], "New question")

    def test_add_question_return_false_if_question_already_exists(self):
        self.assertEqual(self.repository.add_question("New question"), False)

    def test_new_grade_sets_correct_grade(self):
        self.repository.new_grade(1, 5)
        self.assertEqual(self.repository.get_values(1)[0], 5)

    def test_get_questions_functions_correctly(self):
        self.assertEqual(self.repository.get_questions(),
                         [(1, "New question")])

    def test_initalize_database_clears_all_data(self):
        self.repository.initialize_database()
        self.assertEqual(self.repository.get_questions(), [])

    def test_same_question_cant_be_added_twice(self):
        self.assertEqual(self.repository.add_question("New question"), False)

    def test_deactivate_sets_active_question_to_passive(self):
        self.repository.deactive(1)
        self.assertEqual(self.repository.get_questions(), [])