import tkinter as tk
from tkinter import messagebox


class StatusInterface:

    def __init__(self, parent) -> None:
        self.root = tk.Tk()
        self.parent = parent
        self.root.geometry("800x500")
        self.root.title("Daily Questions")

        self._elements()

    def _elements(self):
        exit_btn = tk.Button(self.root, text="Return to main screen",
                             command=self.parent.kill_status_gui).pack()
        questions = self.parent.transmit_questions()
        for question in questions:
            values = self.parent.transmit_answers(question[0])
            qst_lbl = tk.Label(self.root, text=question[1]).pack()
            if values:
                grd_lbl = tk.Label(self.root, text=str(values)).pack()
            else:
                grd_lbl = tk.Label(self.root, text="No answers yet").pack()
            archive_btn = tk.Button(self.root, text="Archive this question",
                                    command=lambda: self._archiver(question[0])).pack()

    def _archiver(self, id):
        self.parent.archive(id)
        messagebox.showinfo("Success!", "Question archived!")

    def kill(self):
        self.root.destroy()

    def activate(self):
        self.root.mainloop()
