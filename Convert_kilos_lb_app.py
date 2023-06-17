# import tkinter module
from tkinter import *
from tkinter.ttk import *
import sv_ttk


def on_conversion_clicked():
    if kilos_label.cget("text") == 'Kilos':
        entry_value = float(value_before_entry.get())
        new_value = entry_value*2.20
        new_value = round(new_value, 3)
        if value_after_entry.get() != '':
            value_after_entry.delete(0, END)
        value_after_entry.insert(0, new_value)
    else:
        entry_value = float(value_before_entry.get())
        new_value = entry_value/2.20
        new_value = round(new_value, 3)
        if value_after_entry.get() != '':
            value_after_entry.delete(0, END)
        value_after_entry.insert(0, new_value)


def on_revert_clicked():
    value_before_entry.delete(0, END)
    value_after_entry.delete(0, END)
    if kilos_label.cget("text") == 'Kilos':
        kilos_label.config(text='lb')
        lb_label.config(text='Kilos')
    else:
        kilos_label.config(text='Kilos')
        lb_label.config(text='lb')


root = Tk()
root.resizable(False, False)

window_width = 200
window_height = 150
root.geometry(f"{window_width}x{window_height}")

kilos_label = Label(root, text="Kilos")
kilos_label.grid(row=0, column=0, columnspan=3)


ConversionButton = Button(root, text="Conversion",
                          command=on_conversion_clicked)
ConversionButton.grid(row=3, column=0, columnspan=1, sticky='we')
ChangeConversionButton = Button(root, text="Revert", command=on_revert_clicked)
ChangeConversionButton.grid(row=3, column=1, columnspan=1, sticky='we')


value_before_entry = Entry(root)
value_before_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=2)

value_after_entry = Entry(root)
value_after_entry.grid(row=4, column=0, columnspan=2, sticky="ew", padx=2)

lb_label = Label(root, text="lb")
lb_label.grid(row=5, column=0, columnspan=3)


combobox = Combobox(root)
combobox['value'] = ('value1', 'value2', 'value3')


root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
# sv_ttk.set_theme("dark")
mainloop()
