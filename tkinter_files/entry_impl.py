from tkinter import *
from tkinter import ttk

def show_message():
    label["text"] = entry.get()
def clear():
    entry.delete(0,END)

root = Tk()
root.geometry("300x300")

entry = ttk.Entry()
entry.pack(anchor=N)

btn = ttk.Button(text="Click", command=show_message)
btn.pack()

clear_btn = ttk.Button(text="clear", command=clear)
clear_btn.pack()

label = ttk.Label()
label.pack()

root.mainloop()