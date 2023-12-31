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
        self.counter = 0
        self.tie = True
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 3

        # Set the window geometry to be centered on the screen
        self.geometry(f"+{x}+{y}")

    def create_buttons(self):

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Roboto slab", 28))
        for i in range(3):
            for j in range(3):
                index = i*3+j
                button = ttk.Button(
                    self, text=" ", command=lambda idx=index, r=i, c=j: self.button_pressed(idx, r, c), style="Custom.TButton")

                button.grid(
                    row=i, column=j, sticky="news")

                self.buttons.append(button)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for j in range(3):
            self.grid_rowconfigure(j, weight=1)

    def button_pressed(self, index, r, c):
        global flag

        if self.buttons[index]["text"] == " " and flag == False:
            flag = True
            self.buttons[index]["text"] = "O"
            self.buttons[index]["state"] = DISABLED
            self.counter += 1
            counter_row_O = 0
            for i in range(3):
                if self.buttons[r*3+i]["text"] == "O":
                    counter_row_O += 1
                else:
                    counter_row_O = 0

            counter_column_O = 0
            for j in range(3):
                if self.buttons[j*3+c]["text"] == "O":
                    counter_column_O += 1
                else:
                    counter_column_O = 0

            counter_diag_O = 0
            counter_diag2_O = 0
            for i in range(3):
                for j in range(3):
                    if i == j:
                        if self.buttons[i*3+j]["text"] == "O":
                            counter_diag_O += 1
                        else:
                            counter_diag_O = 0
                    if i+j == 2:
                        if self.buttons[i*3+j]["text"] == "O":
                            counter_diag2_O += 1
                        else:
                            counter_diag2_O = 0

            if counter_diag_O == 3 or counter_column_O == 3 or counter_row_O == 3 or counter_diag2_O == 3:
                self.print_the_winner(winner="O")
                self.tie = False

        elif self.buttons[index]["text"] == " " and flag == True:
            flag = False
            self.counter += 1
            self.buttons[index]["text"] = "X"
            self.buttons[index]["state"] = DISABLED

            counter_row_X = 0
            for i in range(3):
                if self.buttons[r*3+i]["text"] == "X":
                    counter_row_X += 1
                else:
                    counter_row_X = 0

            counter_column_X = 0
            for j in range(3):
                if self.buttons[j*3+c]["text"] == "X":
                    counter_column_X += 1
                else:
                    counter_column_X = 0

            counter_diag_X = 0
            counter_diag2_X = 0
            for i in range(3):
                for j in range(3):
                    if i == j:
                        if self.buttons[i*3+j]["text"] == "X":
                            counter_diag_X += 1
                        else:
                            counter_diag_X = 0
                    if i+j == 2:
                        if self.buttons[i*3+j]["text"] == "X":
                            counter_diag2_X += 1
                        else:
                            counter_diag2_X = 0

            if counter_diag_X == 3 or counter_column_X == 3 or counter_row_X == 3 or counter_diag2_X == 3:
                self.print_the_winner(winner="X")
                self.tie = False
        self.check_for_draw()

    def check_for_draw(self):

        print(self.counter)
        print(self.tie)
        if self.counter == 9 and self.tie:
            self.print_the_winner(winner="Tie")

    def print_the_winner(self, winner):

        new_window = Toplevel(self)
        new_window.title("Winner tab")
        new_window.grab_set()
        prev_x = self.winfo_x()
        prev_y = self.winfo_y()
        prev_width = self.winfo_width()
        prev_height = self.winfo_height()

        new_x = prev_x + (prev_width - new_window.winfo_reqwidth()) // 2
        new_y = prev_y + (prev_height - new_window.winfo_reqheight()) // 2

        # Place the new window at the calculated position
        new_window.geometry(f"+{new_x}+{new_y}")

        if winner != "Tie":
            label = ttk.Label(new_window, text=f"The winner is {winner}")
            label.pack()
        else:
            label = ttk.Label(new_window, text=f"Its a Tie")
            label.pack()

        restart_button = ttk.Button(
            new_window, text="Restart", command=self.restart)
        quit_button = ttk.Button(new_window, text="Quit", command=self.quit)
        restart_button.pack()
        quit_button.pack()

    def restart(self):
        self.destroy()
        new_window = TicTacToeApp()
        new_window.mainloop()

    def quit(self):
        quit()


if __name__ == '__main__':
    app = TicTacToeApp()
    app.mainloop()
