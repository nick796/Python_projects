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

        self.button_yes = ttk.Button(self.my_frame1, text="Yes", command=self)
        self.button_no = ttk.Button(self.my_frame1, text="No", command=self)

        self.button_yes.grid(row=0, column=0, sticky="we", padx=50, pady=10)
        self.button_no.grid(row=0, column=1, sticky="ew", padx=50, pady=10)

        self.Stats_label = ttk.Label(
            self.my_frame1, text="Stats", style="Custom.TLabel")
        self.Stats_label.grid(row=1, columnspan=2, sticky="wen", padx=100)

        self.my_frame1.grid_columnconfigure(0, weight=1)
        self.my_frame1.grid_columnconfigure(1, weight=1)

        # Start the main thing
        self.start_question()

    def start_question(self):
        with open('data.csv', 'r') as file:
            self.csv_data = list(csv.reader(file))
            # print(self.csv_data)

            self.row_count = sum(1 for _ in self.csv_data)
            random_row = random.randint(1, self.row_count)
            # print("the random row to delete is: ", random_row)

            self.text_panel.insert("1.0", self.csv_data[random_row-1][0])

            self.csv_data.pop(random_row-1)
            # print("New cvs: ", self.csv_data)


if __name__ == '__main__':
    app = Question_app()
    app.mainloop()
