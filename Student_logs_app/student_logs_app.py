from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
import sqlite3
from add_student_class import add_student
from db_config_class import db_config
import random
import string


class Student_log_App(Tk):
    def __init__(self):
        super().__init__()
        # Creating and potisition the  first window
        self.title("Students_Log")
        self.geometry("350x400")
        #self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 4
        y = (screen_height - self.winfo_reqheight()) // 4
        self.geometry(f"+{x}+{y}")
        
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        
        # total_columns_self = self.grid_size()[0]
        # total_rows_self = self.grid_size()[1]
  
        # # Set the empty rows and columns to expand and center the button
        # for row in range(total_rows_self):
        #     self.grid_rowconfigure(row, weight=1)

        # for col in range(total_columns_self):
        #     self.grid_columnconfigure(col, weight=1)
        
        
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = ttk.Frame(self,style="Custom.TFrame")
        self.my_frame.grid(row=0,column=0 ,sticky="nswe")
        
  
        self.my_frame.grid_columnconfigure(0,weight=1)
        self.my_frame.grid_rowconfigure(0,weight=0)

        # Styles
        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=("Roboto slab", 13),anchor=CENTER)
        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 13))
        style4 = ttk.Style()
        style4.configure("Custom.TFrame", background="#dda15e")
        # Creating the first Frame
       
        self.create_labels()
        self.create_buttons()
        
    def create_labels(self):
        self.mauitologio=ttk.Label(self.my_frame ,text="Μαθητολόγιο", style="Custom.TLabel")
        self.mauitologio.grid(row=0, column=0,sticky="nwe"  )
    
    def create_buttons(self):
        self.add_student = ttk.Button(self.my_frame ,text="Προσθήκη Μαθητή",command=self.add_new_student,style="Custom.TButton")
        self.add_student.grid(row=1, column=0,sticky="we ",pady=5,padx=15 )
        
        self.information = ttk.Button(self.my_frame ,text="Βάση Δεδομένων",style="Custom.TButton",command=self.information)
        self.information.grid(row=2, column=0,sticky="we",pady=5 ,padx=15)
    
    def add_new_student(self):
        new_student_window = add_student()
    
    def information(self):
        data_base_db = db_config()
        # self.cursor.execute('SELECT * FROM students')
        # rows = self.cursor.fetchall()
        # for row in rows:
        #     print(row)
      
      
if __name__ == '__main__':
    app = Student_log_App()
    app.mainloop()
