from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
import subprocess
import os
import sv_ttk


class EntryToFileApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("Entry To File App")
        self.geometry("800x600")

        style = ttk.Style()
        style.configure("My_label.TLabel", font=("Roboto slab", 12),
                        foreground="blue", background="yellow")
        self.task_label = ttk.Label(
            self, text="Put the text you want to save to a file", style="My_label.TLabel")
        self.task_label.grid(row=0, column=0, columnspan=2)

        self.task_scrolled_text = scrolledtext.ScrolledText(
            wrap=WORD, font=("Roboto slab", 12))
        self.task_scrolled_text.grid(
            row=1, column=0, columnspan=2, sticky="we", padx=10, pady=5)

        self.save_button = Button(
            self, text="Save", command=self.save)
        self.save_button.grid(row=2, column=0, sticky="nswe")

        self.save_as_button = Button(text="Save as", command=self.save_as)
        self.save_as_button.grid(
            row=2, column=1, sticky="nswe")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def save_as(self):
        content = self.task_scrolled_text.get("1.0", END)
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files ", "*.txt"), ("Pdf Files ", "*.pdf")])
        if filename:
            with open(filename, 'a') as file:
                file.write(content)

    def save(self):
        content = self.task_scrolled_text.get("1.0", END)
        with open("mydata.txt", 'a') as file:
            file.write(content)


if __name__ == '__main__':
    app = EntryToFileApp()
    app.mainloop()
