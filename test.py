from tkinter import *
from tkinter import ttk


class To_Do_List_App(Tk):
    def __init__(self):
        super().__init__()
        self.title("To_Do_List")
        self.geometry("1000x600")
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.counter = 0
        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 3
        self.geometry(f"+{x}+{y}")

        # Frames
        self.my_frame_1 = ttk.Frame(self, style="Custom.TFrame")
        self.my_frame_1.grid(row=0, column=1, sticky='nswe')

        # Styles
        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Roboto slab", 15))

        style2 = ttk.Style()
        style2.configure("Custom.TEntry", font=("Roboto slab", 12))

        style3 = ttk.Style()
        style3.configure("Custom.TButton", font=("Roboto slab", 15))

        style4 = ttk.Style()
        style4.configure("Custom.TFrame", background="#dda15e")
        # Create GUI
        self.create_labels()
        self.create_entries()
        self.create_buttons()

        # Row-Column configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.my_frame_1.grid_columnconfigure(0, weight=1)
        self.my_frame_1.grid_columnconfigure(1, weight=1)
        self.my_frame_1.grid_rowconfigure(1, weight=1)
        self.my_frame_1.grid_rowconfigure(1, weight=1)

        # text
        self.my_td_text = Text(self)
        self.my_td_text.grid(row=1, column=1, sticky="s")
        self.my_td_text.bind("<Button-1>", self.highlight_line)

        # Tag Configure
        self.my_td_text.tag_configure("highlight", background="#dda15e")
        self.my_td_text.tag_configure("strikethrough", overstrike=True)

    def create_labels(self):
        self.your_task_label = ttk.Label(
            self.my_frame_1, style="Custom.TLabel", text="Your task")
        self.your_task_label.grid(row=0, column=0)

    def create_entries(self):
        self.your_entry = ttk.Entry(
            self.my_frame_1, style="Custom.TEntry", width=30)
        self.your_entry.configure(font=("Roboto slab", 15))
        self.your_entry.grid(row=1, column=0)

    def create_buttons(self):
        self.add_button = ttk.Button(
            self.my_frame_1, text="+", style="Custom.TButton", command=self.add_note)
        self.add_button.grid(row=1, column=1, sticky="w")

        self.save_button = ttk.Button(
            self, text="Save", style="Custom.TButton")
        self.save_button.grid(row=2, column=0)

        self.delete_button = ttk.Button(
            self, text="Delete", style="Custom.TButton", command=self.toggle_strikethrough)
        self.delete_button.grid(row=2, column=2)

    def highlight_line(self, event):
        line_index = self.my_td_text.index(
            "@%d,%d linestart" % (event.x, event.y))
        self.my_td_text.tag_remove("highlight", 1.0, "end")
        self.my_td_text.tag_add("highlight", line_index + "linestart",
                                line_index + " lineend")

    def add_note(self):
        your_note = self.your_entry.get()
        self.counter += 1
        line_number = str(self.counter) + "."
        self.my_td_text.insert("end", line_number + " " + your_note + "\n")

    def toggle_strikethrough(self):
        # Get the currently selected text range
        sel_range = self.my_td_text.tag_ranges("sel")

        if sel_range:
            # Toggle the "strikethrough" tag for the selected range
            if "strikethrough" in self.my_td_text.tag_names(sel_range[0]):
                self.my_td_text.tag_remove(
                    "strikethrough", sel_range[0], sel_range[1])
            else:
                self.my_td_text.tag_add(
                    "strikethrough", sel_range[0], sel_range[1])


if __name__ == '__main__':
    app = To_Do_List_App()
    app.mainloop()
