from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import random
import time


'''
TODO: Give the user the option to select 10/20/30 questions
TODO: Have sectors for the question(Chapter1/2/3 etc)
TODO: Polish and create_questions

TODO:(Optional) HighScore

TODO:(Difficult and Optional) find a way to make it in the web 
'''


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
            self.max_row_count = sum(1 for _ in self.csv_data)
        # Logs for the numbers
        self.correct_answers = 0
        self.question_counter = 0

        self.selected_questions_count = 0
        self.the_game_has_started = False
        self.sampled_questions = []

        # Widgets Creation
        self.my_frame1 = ttk.Frame(self, style="Custom.TFrame")
        self.my_frame1.grid(row=1, column=0, sticky="wesn")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.text_panel = Text(self, height=8, font=("Roboto slab", 12))
        self.text_panel.grid(row=0, column=0,
                             sticky="nwe", padx=20, pady=20)

        self.button_yes = ttk.Button(
            self.my_frame1, text="Yes", style="Custom.TButton", command=lambda answer="Yes": self.answer_button(answer, self.button_yes, self.button_no))
        self.button_no = ttk.Button(
            self.my_frame1, text="No", style="Custom.TButton", command=lambda answer="No": self.answer_button(answer, self.button_no, self.button_yes))

        self.button_yes.grid(row=0, column=0, sticky="we", padx=50, pady=10)
        self.button_no.grid(row=0, column=1, sticky="ew", padx=50, pady=10)

        self.Stats_label = ttk.Label(
            self.my_frame1, text="Stats", style="Custom.TLabel")
        self.Stats_label.grid(row=1, columnspan=2, sticky="wen", padx=100)

        self.my_frame1.grid_columnconfigure(0, weight=1)
        self.my_frame1.grid_columnconfigure(1, weight=1)

        self.my_frame2 = ttk.Frame(self.my_frame1, style="Custom.TFrame")

        self.my_frame2.grid(row=2, column=0, columnspan=3,
                            sticky="wen", pady=20)
        self.my_frame2.grid_columnconfigure(0, weight=1)
        self.my_frame2.grid_columnconfigure(1, weight=1)
        self.my_frame2.grid_columnconfigure(2, weight=1)

        self.button_10 = ttk.Button(
            self.my_frame2, text="10 Question", style="Custom.TButton", command=lambda: self.start_with_x_questios(10))
        self.button_10.grid(row=0, column=0)
        self.button_20 = ttk.Button(
            self.my_frame2, text="20 Question", style="Custom.TButton", command=lambda: self.start_with_x_questios(20))
        self.button_20.grid(row=0, column=1)
        self.button_30 = ttk.Button(
            self.my_frame2, text="30 Question", style="Custom.TButton", command=lambda: self.start_with_x_questios(30))
        self.button_30.grid(row=0, column=2)

        # Start the fun
        self.create_style()
        self.start_question()

    def create_style(self):
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
            "Roboto slab", 13), foreground="#239B56")
        style_correct.map("Correct.TButton", foreground=[
                          ("disabled", "#239B56")])

        style4 = ttk.Style()
        style4.configure("Custom.TFrame", background="#dda15e")

    def start_with_x_questios(self, number):
        self.the_game_has_started = True
        with open('data.csv', 'r') as file:
            self.sampled_questions = random.sample(self.csv_data, number)

        self.correct_answers = 0
        self.question_counter = 0

        self.selected_questions_count = number
        self.max_row_count = number
        self.start_question()

    def answer_button(self, answer, pressed_button, other_button):
        # Check if the answer is correct or not
        if (self.sampled_questions[self.random_row-1][1] == f"{answer}") and (pressed_button.cget("text") == f"{answer}"):

            pressed_button.configure(style="Correct.TButton")
            other_button.configure(style="Wrong.TButton")
            self.correct_answers += 1
        else:
            pressed_button.configure(style="Wrong.TButton")
            other_button.configure(style="Correct.TButton")

        self.button_yes.state(["disabled"])
        self.button_no.state(["disabled"])
        self.sampled_questions.pop(self.random_row-1)

        self.after(2000, self.start_question)

    def start_question(self):

        self.button_no.state(["!disabled"])
        self.button_yes.state(["!disabled"])

        self.question_counter += 1
        self.update_stats()
        self.text_panel.delete("1.0", END)
        try:
            self.row_count = sum(1 for _ in self.sampled_questions)
            self.random_row = random.randint(1, self.row_count)
            self.text_panel.insert(
                "1.0", f"Question number: {self.question_counter}\n")
            self.text_panel.insert(
                "2.0", "\n"+self.sampled_questions[self.random_row-1][0])

        except:
            self.button_no.state(["disabled"])
            self.button_yes.state(["disabled"])
            if self.the_game_has_started == False:
                self.text_panel.insert(
                    "1.0", "\n Choose one of the three categories. Thanks")
            elif self.sampled_questions == []:
                self.text_panel.insert("1.0", "\n The questions are finished\n" +
                                       f"You have a success rate of {self.correct_answers/self.max_row_count*100}%")

        self.text_panel.tag_add("center", "1.0", END)
        self.text_panel.tag_configure("center", justify="center")

        self.button_yes.configure(style="Custom.TButton")
        self.button_no.configure(style="Custom.TButton")

    def update_stats(self):
        self.Stats_label.configure(
            text=f"Correct {self.correct_answers}/{self.max_row_count}")


if __name__ == '__main__':
    app = Question_app()
    app.mainloop()
