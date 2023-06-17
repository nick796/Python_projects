import tkinter as tk

root = tk.Tk()

# Create a 3x3 matrix of buttons
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=f"Button {i+1},{j+1}")
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    matrix.append(row)
print(matrix)
root.mainloop()
