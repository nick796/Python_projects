from tkinter import *


class MyApp:
    def __init__(self, master):
        self.master = master
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j
                button = Button(self.master, text=f"Button {idx+1}")
                button.grid(row=i, column=j)
                button.config(command=self.button_pressed(idx))
                self.buttons.append(button)

    def button_pressed(self, idx):
        def callback():
            self.buttons[idx].config(text=f"Button {idx+1} Pressed")
        return callback


root = Tk()
app = MyApp(root)
root.mainloop()
