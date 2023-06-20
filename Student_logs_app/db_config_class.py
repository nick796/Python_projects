from tkinter import *
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
import random
import string
import sqlite3
from tkinter import messagebox  

class db_config(Toplevel):
    def __init__(self):
        super().__init__()
        # Creating and potisition the  first window
        self.title("Πληροφορίες Βάσης Δεδομένων")
        self.geometry("1200x800")
        # self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 4
        y = (screen_height - self.winfo_reqheight()) // 4
        self.geometry(f"+{x}+{y}")
        
        remove_button = ttk.Button(self, text="Delete_Entry", command=self.delete_entry)
        remove_button.pack(pady=10)
    
        # Connect to the database
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        
        # Styles
        style1 = ttk.Style()
        style1.configure("Custom.TLabel", font=("Roboto slab", 13) )
        
        style2 = ttk.Style()
        style2.configure("Custom.TButton", font=("Roboto slab", 13))
        
         # Create a Treeview widget to display the data
        self.treeview = ttk.Treeview(self)
        self.treeview.pack(fill=BOTH, expand=True)
        
        # Fetch all rows from the table
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        
         
        
        # Get the column names
        column_names = [description[0] for description in self.cursor.description[1:]]
        
        # Configure the Treeview with column names
        self.treeview["columns"] = column_names
        self.treeview.heading("#0", text="ID")
        for column in column_names:
            self.treeview.heading(column, text=column)
        
        # Insert data into the Treeview
        for row in rows:
            self.treeview.insert("", END, text=row[0], values=row[1:])
        
   
        # Close the database connection
        self.connection.close()
    
    def delete_entry(self):
      selected_item = self.treeview.selection()
      if selected_item:
        # Get the selected item's ID
        item_id = self.treeview.item(selected_item)['text']

        # Connect to the database
        self.database_connection = sqlite3.connect("students.db")
        self.c = self.database_connection.cursor()

        # Delete the row from the table based on the ID
        self.c.execute("DELETE FROM students WHERE ID=?", (item_id,))

        # Commit the changes to the database
        self.database_connection.commit()

        # Remove the selected item from the Treeview
        self.treeview.delete(selected_item)

        # Close the database cursor and connection
        self.c.close()
        self.database_connection.close()
      else:
        messagebox.showinfo("No Selection", "Please select an entry to delete.")
            
if __name__ == '__main__':
    app = db_config( )
    app.mainloop()

