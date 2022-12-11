import tkinter as tk
from tkinter import messagebox

class GradeInterface:

    def __init__(self,parent) -> None:
        self.root = tk.Tk()
        self.parent = parent
        self.root.geometry("800x500")
        self.root.title("Daily Questions")

        self.grade_var = tk.StringVar()

        self.question_set = self.parent.transmit_questions()

        self.elements()
        self.packer()

    def update_question(self):
        if self.question_set:
            self.current = self.question_set.pop(0)
            self.question_lbl.config(text=self.current[1])
            self.submit_grade_btn.config(default="normal")
        else:
            self.question_lbl.config(text="No questions to grade!")
            self.submit_grade_btn.config(state="disabled")
            exit_btn = tk.Button(self.root, text="Exit", command=self.parent.kill_grade_gui)
            exit_btn.pack()

    def store_grade(self):
        grade = self.grade_var.get()
        if self.parent.grade_question(self.current[0], grade):
            self.grade_var.set("")
            self.update_question()
        else:
            messagebox.showerror("Error!", "Invalid grade!")
    
    def activate_grade(self):
        self.submit_grade_btn.config(text="Submit grade", command=self.store_grade)
        self.grade_entry.config(state="normal")
        self.update_question()

    def elements(self):
        self.question_lbl = tk.Label(self.root, text="""Grade each question with number
         between 1 and 10. Start by clicking 'start'""")
        self.grade_entry = tk.Entry(self.root, textvariable=self.grade_var, state="disabled")
        self.submit_grade_btn = tk.Button(
        self.root, text="Start", command=self.activate_grade, default="normal")

    def packer(self):
        self.question_lbl.pack()
        self.grade_entry.pack()
        self.submit_grade_btn.pack()

    def activate(self):
        self.root.mainloop()

    def kill(self):
        self.root.destroy()