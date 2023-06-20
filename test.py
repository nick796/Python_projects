import tkinter as tk
from tkinter import ttk


class Student_log_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Students_Log")
        self.geometry("250x400")
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) // 4
        y = (self.winfo_screenheight() - self.winfo_reqheight()) // 4
        self.geometry(f"+{x}+{y}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=("Roboto slab", 15))
        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 15))

        self.create_labels()
        self.create_buttons()

    def create_labels(self):
        mauitologio = ttk.Label(self, text="Μαθητολόγιο", style="Custom.TLabel")
        mauitologio.grid(row=0, column=0, sticky="n")

    def create_buttons(self):
        add_student = ttk.Button(self, text="Προσθήκη Μαθητή", style="Custom.TButton")
        add_student.grid(row=0, column=0, sticky="nsew", pady=40, padx=15)

        information = ttk.Button(self, text="Πληροφορίες Μαθητή", style="Custom.TButton")
        information.grid(row=0, column=0, sticky="nsew", pady=90, padx=15)


if __name__ == '__main__':
    app = Student_log_App()
    app.mainloop()
