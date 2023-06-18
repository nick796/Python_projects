from tkinter import *
from tkinter import ttk
import random
import string


class PlaceholderSpinbox(ttk.Spinbox):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.default_style = self.cget("style")
        self.set_placeholder()

        self.bind("<FocusIn>", self.clear_placeholder)
        self.bind("<FocusOut>", self.set_placeholder)

    def set_placeholder(self, event=None):
        if not self.get():
            self.set(self.placeholder)
            self.configure(style="Placeholder.TSpinbox")

    def clear_placeholder(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.configure(style=self.default_style)


class PasswordGeneratorApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password_Generator")
        self.geometry("900x200")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 3
        self.geometry(f"+{x}+{y}")

        self.create_labels()
        self.create_spinboxes()
        self.create_button()

        print(string.ascii_lowercase)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Roboto slab", 12))
        style2 = ttk.Style()
        style2.configure("Placeholder.TSpinbox", font=("Roboto slab", 14))
        style3 = ttk.Style()
        style3.configure("Button.TButton", font=("Roboto slab", 12))

    def create_labels(self):
        number_char_Label = ttk.Label(
            self, style="Custom.TLabel", text="Number of characters")
        number_char_Label.grid(row=0, column=0, sticky="s", pady=20)

        number_uppercase_Label = ttk.Label(
            self, style="Custom.TLabel", text="Number of Uppercase chars")
        number_uppercase_Label.grid(row=0, column=1, sticky="s", pady=20)

        number_symbols_Label = ttk.Label(
            self, style="Custom.TLabel", text="Number of symbols")
        number_symbols_Label.grid(row=0, column=2, sticky="s", pady=20)

        number_numbers_Label = ttk.Label(
            self, style="Custom.TLabel", text="Numbers")
        number_numbers_Label.grid(row=0, column=3, sticky="s", pady=20)

    def create_spinboxes(self):

        self.num_char_spinbox = PlaceholderSpinbox(
            self, from_=1, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        self.num_char_spinbox.grid(row=1, column=0, sticky="n")

        self.number_uppercase_char_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        self.number_uppercase_char_spinbox.grid(row=1, column=1, sticky="n")

        self.number_symbols_char_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        self.number_symbols_char_spinbox.grid(row=1, column=2, sticky="n")

        self.number_numbers_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        self.number_numbers_spinbox.grid(row=1, column=3, sticky="n")

    def create_button(self):
        self.button = ttk.Button(self, text="Create",
                                 command=self.create_pass, padding=10, style="Button.TButton")
        self.button.grid(row=2, columnspan=4, sticky="n")

    def create_pass(self):
        num_char_value = self.num_char_spinbox.get()
        num_uppercase_value = self.number_uppercase_char_spinbox.get()
        num_symbols_value = self.number_symbols_char_spinbox.get()
        num_numbers_value = self.number_numbers_spinbox.get()

        password_length = int(num_char_value)
        uppercase_chars = int(num_uppercase_value)
        symbol_chars = int(num_symbols_value)
        number_chars = int(num_numbers_value)

        lowercase_chars = password_length - uppercase_chars - symbol_chars - number_chars
        lowercase_letters = string.ascii_lowercase
        password = ''.join(random.choice(lowercase_letters)
                           for _ in range(lowercase_chars))

        # Generate uppercase characters
        uppercase_letters = string.ascii_uppercase
        password += ''.join(random.choice(uppercase_letters)
                            for _ in range(uppercase_chars))

        # Generate symbol characters
        symbols = "!@#%"
        password += ''.join(random.choice(symbols)
                            for _ in range(symbol_chars))

        # Generate number characters
        numbers = string.digits
        password += ''.join(random.choice(numbers)
                            for _ in range(number_chars))

        # Shuffle the password to randomize the character order
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        new_window = Toplevel(self)
        new_window.title("The password ")
        new_window.grab_set()
        prev_x = self.winfo_x()
        prev_y = self.winfo_y()
        prev_width = self.winfo_width()
        prev_height = self.winfo_height()

        new_x = prev_x + (prev_width - new_window.winfo_reqwidth()) // 2
        new_y = prev_y + (prev_height - new_window.winfo_reqheight()) // 2

        # Place the new window at the calculated position
        new_window.geometry(f"+{new_x}+{new_y}")

        label = ttk.Label(new_window, text=f"Your password is {password}")
        label.pack()

        restart_button = ttk.Button(
            new_window, text="Restart", command=self.restart)
        quit_button = ttk.Button(new_window, text="Quit", command=self.quit)
        restart_button.pack()
        quit_button.pack()

        print("Generated Password:", password)

    def restart(self):
        self.destroy()
        new_window = PasswordGeneratorApp()
        new_window.mainloop()


if __name__ == '__main__':
    app = PasswordGeneratorApp()
    app.mainloop()
