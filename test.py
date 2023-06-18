from tkinter import *
from tkinter import ttk
import random
import string

lowercase_chars = 5
lowercase_letters = "abcdefg"
password = ''.join(random.choice(lowercase_letters)
                   for _ in range(lowercase_chars))

print(password)
password_list = list(password)
print(password_list)
