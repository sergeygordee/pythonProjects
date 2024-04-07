from itertools import chain
from tkinter import ttk
from tkinter import *

root = Tk()
root.geometry("300x300")
python = "Python"
java = "Java"
c = "c"
lang = StringVar(value=java)
python_img =PhotoImage(file="qwe.png")
java_img =PhotoImage(file="qwe.png")
c_img =PhotoImage(file="qwe.png")

python_btn = (
    ttk.Radiobutton(value=python, variable=lang, image=python_img))
python_btn.pack()
java_btn = (
    ttk.Radiobutton(value=java, variable=lang, image=java_img))
java_btn.pack()
c_btn = (
    ttk.Radiobutton(value=c, variable=lang, image=c_img))
c_btn.pack()
root.mainloop()