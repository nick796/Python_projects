from tkinter import *
from tkinter import ttk


class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Adjustable Height Spinbox")
        self.geometry("400x200")

        spinbox = ttk.Spinbox(self, from_=1, to=12, font=("Arial", 12))
        spinbox.grid(row=0, column=0, padx=10, pady=(20, 10))
        spinbox.config(padding=(10, 5))  # Adjust the top and bottom padding


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
