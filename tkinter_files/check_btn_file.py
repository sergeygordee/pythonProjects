from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")

'''enabled = IntVar()

enabled_btn = ttk.Checkbutton(text="turn on", variable=enabled)
enabled_btn.pack()

enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack()'''

def select():
    result = "selected: "
    if python.get() == 1:
        result = f"{result} Python"
    if java.get() == 1:
        result = f"{result} Java"
    if c.get() == 1:
        result = f"{result} C"
    languages.set(result)

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack()

python = IntVar()
python_btn = ttk.Checkbutton(text="Python", variable=python,command=select)
python_btn.pack()

java = IntVar()
java_btn = ttk.Checkbutton(text="Java", variable=java,command=select)
java_btn.pack()

c = IntVar()
c_btn = ttk.Checkbutton(text="C", variable=c,command=select)
c_btn.pack()
root.mainloop()