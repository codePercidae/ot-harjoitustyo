import tkinter as tk
from tkinter import messagebox

class Interface:

    def __init__(self, parent) -> None:
        self.root = tk.Tk()
        self.parent = parent
        self.question_var = tk.StringVar()
        self.grade_var = tk.StringVar()

        self.root.geometry("800x500")

        self.root.title("Daily Questions")
        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
    
        settings_menu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings_menu)


        settings_menu.add_command(label="Empty data", command=self.empty_data)

        greeting = tk.Label(self.root, text="Are you ready to answer your daily questions?",pady=20)

        grade_btn = tk.Button(self.root, text="start grading", command=self.grade_window,pady=10)

        new_question = tk.Label(self.root, text="Or give a new daily question.", pady=10)
        
        greeting.pack()

        grade_btn.pack()
        
        new_question.pack()

        newq = tk.Entry(self.root, textvariable=self.question_var)
        
        newq.pack()

        submit_btn = tk.Button(self.root, text="add question", command= self.store_entry, pady=10)

        submit_btn.pack()
        
        self.question_set = []
    
    def activate(self):
        self.root.mainloop()

    def store_entry(self):
        question = self.question_var.get()
        if self.parent.new_question(question):
            messagebox.showinfo("Success", "Question added!")
        else: messagebox.showerror("ERROR", "Something went wrong! Maybe the question already exists or developer has managed to corrupt the filesystem ¯\_(ツ)_/¯")
        self.question_var.set("")

    def empty_data(self):
        check = messagebox.askquestion("Warning!", "Are you sure you wish to delete all data?")
        if check == "yes":
            self.parent.empty_database()
        messagebox.showinfo("Success!","All data erased!")

        
    def grade_window(self):
        #Needs refactoring
        new_window = tk.Toplevel(self.root)
        new_window.geometry("800x500")
        question_lbl = tk.Label(new_window, text="No questions to grade")
        question_lbl.pack()
        grade_entry = tk.Entry(new_window, textvariable=self.grade_var)
        grade_entry.pack()
        self.question_set = self.parent.transmit_questions()
        if self.question_set:
            question_lbl.config(text=self.question_set.pop(0)[1])

        def store_grade():
            submit_grade_btn.configure(default="normal")
            grade = self.grade_var.get()
            self.grade_var.set("")
            if self.question_set:
                new_question = self.question_set.pop(0)
                question_lbl.config(text=new_question[1])
                self.parent.grade_question(new_question[0], grade)
            else:
                question_lbl.config(text="All questions answered!")
                submit_grade_btn["state"] = "disabled"

        
        submit_grade_btn = tk.Button(new_window, text="Save answer", command=store_grade, default="disabled")
        submit_grade_btn.pack()