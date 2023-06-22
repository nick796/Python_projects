from tkinter import *
from tkinter import ttk
root = Tk()

style = ttk.Style()
style.configure('TButton', foreground='red')
bu1 = ttk.Button(root, text="Hello world")
bu1.grid(row=0, column=0)

bu2 = ttk.Button(root, text="Hello world2")
bu2.grid(row=1, column=0)
style.map(
    "TButton",
    foreground=[("disabled", "red")]
)
bu1.state(['disabled'])
bu2.state(['disabled'])

root.mainloop()
