import tkinter as tk
from tkinter import messagebox


class Interface:

    def __init__(self, parent) -> None:
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Daily Questions")

        self.parent = parent

        self._question_var = tk.StringVar()

        self._init_menu()
        self._elements()
        self._packer()

    def activate(self):
        self.root.mainloop()

    def _init_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Empty data", command=self._empty_data)

    def _elements(self):
        self.greeting = tk.Label(
            self.root, text="Are you ready to answer your daily questions?", pady=20)

        self.grade_btn = tk.Button(self.root, text="start grading",
                                   command=self._grading, pady=10)

        self.insert_question = tk.Label(
            self.root, text="Or give a new daily question.", pady=10)

        self.new_question = tk.Entry(
            self.root, textvariable=self._question_var)

        self.submit_btn = tk.Button(
            self.root, text="add question", command=self._store_entry, pady=10)

        self.status_btn = tk.Button(
            text="Question status", command=self.parent.status_window)

    def _packer(self):
        self.greeting.pack()

        self.grade_btn.pack()

        self.insert_question.pack()

        self.new_question.pack()

        self.submit_btn.pack()

        self.status_btn.pack()

    def _store_entry(self):
        question = self._question_var.get()
        if self.parent.new_question(question):
            messagebox.showinfo("Success", "Question added!")
        else:
            messagebox.showerror(
                "ERROR", """Something went wrong! Too many active questions, invalid question or given 
question already exists!""")
        self._question_var.set("")

    def _empty_data(self):
        check = messagebox.askquestion(
            "Warning!", "Are you sure you wish to delete all data?")
        if check == "yes":
            self.parent.empty_database()
        messagebox.showinfo("Success!", "All data erased!")

    def _grading(self):
        self.parent.grade_window()

    def kill(self):
        self.root.destroy()
