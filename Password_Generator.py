from tkinter import *
from tkinter import ttk


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

        num_char_spinbox = PlaceholderSpinbox(
            self, from_=1, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        num_char_spinbox.grid(row=1, column=0, sticky="n")

        number_uppercase_char_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        number_uppercase_char_spinbox.grid(row=1, column=1, sticky="n")

        number_symbols_char_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        number_symbols_char_spinbox.grid(row=1, column=2, sticky="n")

        number_numbers_spinbox = PlaceholderSpinbox(
            self, from_=0, to=12, style="Placeholder.TSpinbox", placeholder="Select a value")
        number_numbers_spinbox.grid(row=1, column=3, sticky="n")

    def create_button(self):
        button = ttk.Button(self, text="Create",
                            command=self.create_pass, padding=10, style="Button.TButton")
        button.grid(row=2, columnspan=4, sticky="n")

    def create_pass(self):
        pass


if __name__ == '__main__':
    app = PasswordGeneratorApp()
    app.mainloop()
