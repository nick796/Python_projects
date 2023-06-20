from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
import random
import string
import sqlite3

class add_student(Toplevel):
    def __init__(self):
        super().__init__()
        # Creating and positioning the first window
        self.title("Στοιχεία Μαθητή")
        self.geometry("600x400")
        # self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 4
        y = (screen_height - self.winfo_reqheight()) // 4
        self.geometry(f"+{x}+{y}")


        # Styles
        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=("Roboto slab", 13) )

        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 13))

        self.grid_columnconfigure(1,weight=1)

        # Labels
        self.general = ttk.Label(self,text="Στοιχεία μαθητή",style="Custom.TLabel")
        self.general.grid(row=0,column=0,sticky=" n",columnspan=2)
        self.name = ttk.Label(self, text="Όνομα",style="Custom.TLabel")
        self.name.grid(row=1,column=0)
        self.surname=ttk.Label(self, text="Επίθετο",style="Custom.TLabel")
        self.surname.grid(row=2,column=0)
        self.phone=ttk.Label(self, text="Τηλέφωνο",style="Custom.TLabel")
        self.phone.grid(row=3,column=0)
        self.email=ttk.Label(self, text="Email",style="Custom.TLabel")
        self.email.grid(row=4,column=0 )
        self.comments=ttk.Label(self, text="Σχόλια",style="Custom.TLabel")
        self.comments.grid(row=5,column=0)

        # Entries
        self.name_entry = ttk.Entry(self,font=("Roboto slab",12) )
        self.name_entry.grid(row=1,column=1,sticky="we",padx=12,pady=4)

        self.surname_entry=ttk.Entry(self,font=("Roboto slab",12)  )
        self.surname_entry.grid(row=2,column=1,sticky="we",padx=12,pady=4)

        self.phone_entry=ttk.Entry(self,font=("Roboto slab",12) )
        self.phone_entry.grid(row=3,column=1,sticky="we",padx=12,pady=4)

        self.email_entry=ttk.Entry(self,font=("Roboto slab",12)  )
        self.email_entry.grid(row=4,column=1,sticky="we",padx=12,pady=4)

        self.comments_text= Text(self,height=6,font=("Roboto slab",12))
        self.comments_text.grid(row=5,column=1,sticky="we",padx=12,pady=5 )

        # Button
        self.save_button = ttk.Button(self,text="Αποθήκευση Μαθητή",style="Custom.TButton",command=self.save_student)
        self.save_button.grid(row=6,column=0,columnspan=2,pady=5)

    def save_student(self):
        name_inf = self.name_entry.get()
        surname_info= self.surname_entry.get( )
        phone_info= self.phone_entry.get( )
        email_info= self.email_entry.get( )
        comments_info = self.comments_text.get("1.0", "end-1c" )

        database_connection = sqlite3.connect("students.db")
        c = database_connection.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS students(ID INTEGER PRIMARY KEY, ΟΝΟΜΑ TEXT, ΕΠΙΘΕΤΟ TEXT, ΤΗΛΕΦΩΝΟ TEXT, EMAIL TEXT, ΣΧΟΛΙΑ TEXT)")

        c.execute("INSERT INTO students(ΟΝΟΜΑ, ΕΠΙΘΕΤΟ, ΤΗΛΕΦΩΝΟ, EMAIL, ΣΧΟΛΙΑ) VALUES(?,?,?,?,?)",(name_inf,surname_info,phone_info,email_info,comments_info))

        if not name_inf:
            error_message = "Παρακαλώ εισάγετε το όνομα του μαθητή."
            self.show_error_message(error_message, self.name_entry)
            return

        if not surname_info:
            error_message = "Παρακαλώ εισάγετε το επίθετο του μαθητή."
            self.show_error_message(error_message, self.surname_entry)
            return

        if not phone_info:
            error_message = "Παρακαλώ εισάγετε το τηλέφωνο του μαθητή."
            self.show_error_message(error_message, self.phone_entry)
            return

        database_connection.commit()
        database_connection.close()

        message_window = Toplevel(self)
        message_window.title("Επιτυχία")
        message_window.grab_set()
        prev_x = self.winfo_x()
        prev_y = self.winfo_y()
        prev_width = self.winfo_width()
        prev_height = self.winfo_height()

        new_x = prev_x + (prev_width - message_window.winfo_reqwidth()) // 2
        new_y = prev_y + (prev_height - message_window.winfo_reqheight()) // 2

        # Place the new window at the calculated position
        message_window.geometry(f"+{new_x}+{new_y}")
        message_window.geometry("600x100")
        label = ttk.Label( message_window, text=f"O μαθητής/τρια {name_inf} αποθηκεύτηκε επιτυχώς στην βάση δεδομένων!",style="Custom.TLabel")
        label.pack()
        ok_button = ttk.Button( message_window, text=f"OK", command= self.close,style="Custom.TButton")
        ok_button.pack()

    def close(self):
        self.destroy()

    def show_error_message(self,error_message,entry_widget):
        error_window= Toplevel(self)
        error_window.title("Σφάλμα")
        error_window.grab_set()
        error_window.geometry("500x100")
        error_label = ttk.Label( error_window, text=error_message)
         
if __name__ == '__main__':
    app = add_student()
    app.mainloop()
