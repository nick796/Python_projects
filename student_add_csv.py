import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime
from tkinter.messagebox import showerror, showwarning, showinfo
#======================= Window Creation =======================
window = tk.Tk()
window.geometry('600x170')
window.minsize(600,170)
window_grip = ttk.Sizegrip(window ) 
window_grip.place(relx=0.99,rely=0.99,anchor= tk.SE)

window.rowconfigure(0,weight=1,uniform='a')
window.columnconfigure(0,weight=1,uniform='a')

#======================= Label_Frame Creation =======================
label_frame = ttk.LabelFrame(window, text="Στοιχεία Μαθητή")
label_frame.grid(column=0, row=0, padx=10, pady=10,sticky="nesw")

#======================= Create Labels and Entry Widgets =======================
labels = ["Name:", "Email:", "Phone:"]
entries = []

for i, label in enumerate(labels):
    # Create Label
    ttk.Label(label_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    # Create Entry
    entry = ttk.Entry(label_frame)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
    entries.append(entry)

# Adjust column weights to make entries stretchable
label_frame.columnconfigure(1, weight=1)

#=============================Submit Button=========================
def submit_pressed(entries):
    
    # Collecting values from the Entry widgets
    values = [entry.get() for entry in entries]
    
    # Get current time for timestamp (optional)
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Open the CSV file in append mode and check if header is needed
    try:
        # Check if the file exists and is empty
        with open("user_data.csv", "r", newline="") as file:
            first_line = file.readline()
            if not first_line:  # If the file is empty, write the header
                write_header = True
            else:
                write_header = False
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the header
        write_header = True

    # Open the CSV file in append mode
    with open("user_data.csv", "a", newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write the header only if the file was empty or newly created
        if write_header:
            writer.writerow(["Timestamp", "Name", "Email", "Phone"])

        # Write the timestamp and user data as a new row
        writer.writerow([timestamp] + values)

    showinfo(title='Καταχώρηση Μαθητή', message='Η καταχώρηση μαθητή ήταν επιτυχής')
  

submit_button = ttk.Button(label_frame,text='Submit',command=lambda:submit_pressed(entries))
submit_button.grid(row=len(labels), column=0, columnspan=2, padx=5, pady=5)



window.mainloop()