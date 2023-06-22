from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import random


class Question_app(Tk):
    def __init__(self):
        super().__init__()

        self.title("Questions")
        self.geometry("1000x400")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 4
        y = (screen_height - self.winfo_reqheight()) // 10
        self.geometry(f"+{x}+{y}")

        # Read the csvs file
        with open('data.csv', 'r') as file:
            self.csv_data = list(csv.reader(file))

        self.correct_answers = 0
        # Styles
        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=(
            "Roboto slab", 13), anchor=CENTER)
        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 13))
        style4 = ttk.Style()
        style4.configure("Custom.TFrame", background="#dda15e")
        # Creating the first Frame
        self.my_frame1 = ttk.Frame(self, style="Custom.TFrame")
        self.my_frame1.grid(row=1, column=0, sticky="wesn")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.text_panel = Text(self, height=8, font=("Roboto slab", 12))
        self.text_panel.grid(row=0, column=0,
                             sticky="nwe", padx=20, pady=20)

        self.button_yes = ttk.Button(
            self.my_frame1, text="Yes", command=self.yes_func)
        self.button_no = ttk.Button(
            self.my_frame1, text="No", command=self.no_func)

        self.button_yes.grid(row=0, column=0, sticky="we", padx=50, pady=10)
        self.button_no.grid(row=0, column=1, sticky="ew", padx=50, pady=10)

        self.Stats_label = ttk.Label(
            self.my_frame1, text="Stats", style="Custom.TLabel")
        self.Stats_label.grid(row=1, columnspan=2, sticky="wen", padx=100)

        self.my_frame1.grid_columnconfigure(0, weight=1)
        self.my_frame1.grid_columnconfigure(1, weight=1)

        # Start the main thing
        self.start_question()

    def yes_func(self):
        if self.csv_data[self.random_row-1][1] == "Yes":
            self.correct_answers += 1

        self.csv_data.pop(self.random_row-1)
        # print("New cvs: ", self.csv_data)
        self.start_question()

    def no_func(self):

        if self.csv_data[self.random_row-1][1] == "No":
            self.correct_answers += 1
        self.csv_data.pop(self.random_row-1)

        self.start_question()

    def start_question(self):
        self.update_stats()
        self.text_panel.delete("1.0", END)
        try:
            self.row_count = sum(1 for _ in self.csv_data)
            self.random_row = random.randint(1, self.row_count)
            self.text_panel.insert("1.0", self.csv_data[self.random_row-1][0])
        except:
            self.text_panel.insert("1.0", "The questions are finidhed")
            self.button_no.state(["disabled"])
            self.button_yes.state(["disabled"])
         # print("the random row to delete is: ", random_row)

    def update_stats(self):
        self.Stats_label.configure(text=f"Correct {self.correct_answers}/4")


if __name__ == '__main__':
    app = Question_app()
    app.mainloop()
