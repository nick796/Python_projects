from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import random
import time


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
        self.question_counter = 0

        self.my_frame1 = ttk.Frame(self, style="Custom.TFrame")
        self.my_frame1.grid(row=1, column=0, sticky="wesn")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.text_panel = Text(self, height=8, font=("Roboto slab", 12))
        self.text_panel.grid(row=0, column=0,
                             sticky="nwe", padx=20, pady=20)

        self.button_yes = ttk.Button(
            self.my_frame1, text="Yes", style="Custom.TButton", command=self.yes_func)
        self.button_no = ttk.Button(
            self.my_frame1, text="No", style="Custom.TButton", command=self.no_func)

        self.button_yes.grid(row=0, column=0, sticky="we", padx=50, pady=10)
        self.button_no.grid(row=0, column=1, sticky="ew", padx=50, pady=10)

        self.Stats_label = ttk.Label(
            self.my_frame1, text="Stats", style="Custom.TLabel")
        self.Stats_label.grid(row=1, columnspan=2, sticky="wen", padx=100)

        self.my_frame1.grid_columnconfigure(0, weight=1)
        self.my_frame1.grid_columnconfigure(1, weight=1)

 # Styles
        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=(
            "Roboto slab", 13), anchor=CENTER)
        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 13))

        style_wrong = ttk.Style()
        style_wrong.configure("Wrong.TButton", font=(
            "Roboto slab", 13), foreground="#DE3163")
        style_wrong.map("Wrong.TButton", foreground=[("disabled", "#DE3163")])

        style_correct = ttk.Style()
        style_correct.configure("Correct.TButton", font=(
            "Roboto slab", 13), foreground="#9FE2BF")
        style_correct.map("Correct.TButton", foreground=[
                          ("disabled", "#9FE2BF")])

        style4 = ttk.Style()
        style4.configure("Custom.TFrame", background="#dda15e")
        # Creating the first Frame
        # Start the main thing

        self.start_question()

    def yes_func(self):

        if self.csv_data[self.random_row-1][1] == "Yes":
            self.correct_answers += 1
            self.button_yes.configure(style="Correct.TButton")
            self.button_no.configure(style="Wrong.TButton")

        else:
            self.button_yes.configure(style="Wrong.TButton")
            self.button_no.configure(style="Correct.TButton")
        self.button_yes.configure(state=DISABLED)
        self.button_no.configure(state=DISABLED)
        self.csv_data.pop(self.random_row-1)

        self.after(2000, self.start_question)
        # self.start_question()

    def no_func(self):

        if self.csv_data[self.random_row-1][1] == "No":
            self.correct_answers += 1
            self.button_yes.configure(style="Wrong.TButton")
            self.button_no.configure(style="Correct.TButton")

        else:
            self.button_yes.configure(style="Correct.TButton")
            self.button_no.configure(style="Wrong.TButton")

        self.csv_data.pop(self.random_row-1)
        self.button_yes.state(["disabled"])
        self.button_no.state(["disabled"])
        self.after(2000, self.start_question)
        # self.start_question()

    def start_question(self):

        self.button_no.state(["!disabled"])
        self.button_yes.state(["!disabled"])

        self.question_counter += 1
        self.update_stats()
        self.text_panel.delete("1.0", END)
        try:
            self.row_count = sum(1 for _ in self.csv_data)
            self.random_row = random.randint(1, self.row_count)
            self.text_panel.insert(
                "1.0", f"Question number: {self.question_counter}\n")
            self.text_panel.insert(
                "2.0", "\n"+self.csv_data[self.random_row-1][0])

        except:
            self.text_panel.insert("1.0", "\n The questions are finished")
            self.button_no.state(["disabled"])
            self.button_yes.state(["disabled"])

        self.text_panel.tag_add("center", "1.0", END)
        self.text_panel.tag_configure("center", justify="center")

        self.button_yes.configure(style="Custom.TButton")
        self.button_no.configure(style="Custom.TButton")

    def update_stats(self):
        # self.text_panel.insert(
        #     "1.0", f"Question number: {self.question_counter}\n")
        self.Stats_label.configure(text=f"Correct {self.correct_answers}/4")


if __name__ == '__main__':
    app = Question_app()
    app.mainloop()
