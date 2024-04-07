from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")

'''for c in range (3):
    root.columnconfigure(index=c, weight=1)

for r in range (3):
    root.rowconfigure(index=r, weight=1)'''

'''for r in range (3):
    for c in range (3):
        btn = ttk.Button(text=f"{r}, {c}")
        btn.grid(row =r, column = c)'''

'''btn1 = ttk.Button(text="Btn1")
btn1.grid(row = 0, column = 0,
          ipadx =70, columnspan=2, padx=5, pady=5)

btn2 = ttk.Button(text="Btn2")
btn2.grid(row = 1, column = 0, padx=5, pady=5)

btn3 = ttk.Button(text="Btn3")
btn3.grid(row = 1, column = 1, padx=5, pady=5)'''
def entered(event):
    btn["text"] = "Entered"

def left(event):
    btn["text"] = "Left"

btn = ttk.Button(text="btn")
btn.pack(anchor=CENTER)

btn.bind("<Enter>",entered)
btn.bind("<Leave>", left)
root.mainloop()
