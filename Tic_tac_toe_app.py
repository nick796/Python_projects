from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

flag = False


class TicTacToeApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("TicTacToe")
        self.geometry("400x300")
        self.buttons = []
        self.create_buttons()

        self.counter_row_O = 0
        self.counter_column_O = 0
        self.counter_diag_O = 0

        self.counter_row_X = 0
        self.counter_column_X = 0
        self.counter_diag_X = 0

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                index = i*3+j
                button = ttk.Button(
                    self, text=" ", command=lambda idx=index, r=i, c=j: self.button_pressed(idx, r, c))
                button.grid(
                    row=i, column=j, sticky="news")

                self.buttons.append(button)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for j in range(3):
            self.grid_rowconfigure(j, weight=1)
        print(self.buttons)

    def button_pressed(self, index, r, c):
        global flag
        if self.buttons[index]["text"] == " " and flag == False:
            flag = True
            self.buttons[index]["text"] = "0"
            self.buttons[index]["state"] = DISABLED

            counter_row_O = 0
            for i in range(3):
                if self.buttons[r*3+i]["text"] == "0":
                    counter_row_O += 1
                else:
                    counter_row_O = 0

            counter_column_O = 0
            for j in range(3):
                if self.buttons[j*3+c]["text"] == "0":
                    counter_column_O += 1
                else:
                    counter_column_O = 0

            counter_diag_O = 0
            for i in range(3):
                for j in range(3):
                    if i == j:
                        if self.buttons[i*3+j]["text"] == "0":
                            counter_diag_O += 1
                        else:
                            counter_diag_O = 0

            if counter_diag_O == 3 or counter_column_O == 3 or counter_row_O == 3:
                print("0 is the winner")
        elif self.buttons[index]["text"] == " " and flag == True:
            flag = False
            self.buttons[index]["text"] = "X"
            self.buttons[index]["state"] = DISABLED

            counter_row_O = 0
            for i in range(3):
                if self.buttons[r*3+i]["text"] == "X":
                    counter_row_O += 1
                else:
                    counter_row_O = 0

            counter_column_O = 0
            for j in range(3):
                if self.buttons[j*3+c]["text"] == "X":
                    counter_column_O += 1
                else:
                    counter_column_O = 0

            counter_diag_O = 0
            for i in range(3):
                for j in range(3):
                    if i == j:
                        if self.buttons[i*3+j]["text"] == "X":
                            counter_diag_O += 1
                        else:
                            counter_diag_O = 0

            if counter_diag_O == 3 or counter_column_O == 3 or counter_row_O == 3:
                print("X is the winner")

    # def button_pressed(self, index):
    #     def callback():
    #         self.buttons[index].config(text=f"Button {index+1} Pressed")
    #     return callback


if __name__ == '__main__':
    app = TicTacToeApp()
    app.mainloop()
