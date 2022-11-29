from question_repository import QuestionRepository

GUIDE = """To save a new daily question, input n\n
To grade your daily questions, input g\n
To see the previus answers, input s\n
To remove all entries, input FORMAT\n
To exit input, x\n"""


class DailyQuestionsApp:

    def __init__(self) -> None:
        self.repository = QuestionRepository()

    def start(self):
        print(GUIDE)

        while True:
            command = input()

            if command == "n":
                self.new_question()
            elif command == "g":
                self.grade_questions()
            elif command == "s":
                self.show_answers()
            elif command == "FORMAT":
                double_check = input(
                    """Are you sure you want to delete all
                    your questions and answers? y/n: """) == "y"
                if double_check == "y":
                    self.empty_database()
            elif command == "x":
                break
            else:
                print("invalid command")

    def new_question(self):
        question = input("Please insert the question here:\n")
        self.repository.add_question(question)
        print("Question added!")

    def grade_questions(self):
        print("Evaluate your performance on each question from 1 to 10.")

        for question in self.repository.get_questions():
            print(question[1])
            grade = input("Input grade here: ")
            self.repository.new_grade(question[0], grade)

        print("All questions aswered!")

    def show_answers(self):
        questions = self.repository.get_questions()
        for question in questions:
            values = self.repository.get_values(question[0])
            print(question[1])
            print(str(values) + "\n")

    def empty_database(self):
        self.repository.initialize_database()
