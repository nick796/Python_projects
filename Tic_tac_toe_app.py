from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog


class TicTacToeApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("TicTacToe")
        self.geometry("400x300")
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                index = i*3+j
                button = ttk.Button(
                    self, text=f" ", command=lambda idx=index: self.button_pressed(idx))
                button.grid(
                    row=i, column=j, sticky="news")
                self.buttons.append(button)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for j in range(3):
            self.grid_rowconfigure(j, weight=1)

    def button_pressed(self, index):
        if self.buttons[index]["text"] != "0":
            self.buttons[index]["text"] = "0"
        else:
            self.buttons[index]["text"] = "X"

    # def button_pressed(self, index):
    #     def callback():
    #         self.buttons[index].config(text=f"Button {index+1} Pressed")
    #     return callback


if __name__ == '__main__':
    app = TicTacToeApp()
    app.mainloop()
