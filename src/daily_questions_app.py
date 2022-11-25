from question_repository import QuestionRepository
from database_connection import get_database_connection

GUIDE="""To save a new daily question, input n\n
To grade your daily questions, input g\n
To see the previus answers, input s\n
To exit input, x\n"""

class Daily_questions_app:

    def __init__(self) -> None:
        self.repository = QuestionRepository()
    
    def start(self):
        print(GUIDE)
        
        while True:
            command = input()
            
            if command == "n":
                self.new_question()
            elif command =="g":
                self.grade_questions()
            elif command == "s":
                self.show_answers()
            elif command == "x":
                break
            else: print("invalid command")


    def new_question(self):
        question = input("Please insert the question here:\n")
        self.repository.add_question_db(question)
        print("Question added!")
        

    def grade_questions(self):
        print("Evaluate your performance on each question from 1 to 10.")

        for question in self.repository.get_questions():
            print(question)
            question = question.replace(" ", "")
            grade = input("Input grade here: ")
            self.repository.new_grade_db(question, grade)

        print("All questions aswered!")

    def show_answers(self):
        for question, answers in self.repository.get_questions().items():
            print(question)
            print(", ".join(answers))