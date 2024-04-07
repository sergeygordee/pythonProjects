import re
from tkinter import *
from tkinter import ttk
import re

root = Tk()
root.geometry("300x300")
def is_valid(newval):
    result = re.match("^\+\d{0,11}$", newval) is not None
    if not result and len(newval) <=12:
        errmsg.set("Number is not correct")
    else:
        errmsg.set("")
    return result
check = (root.register(is_valid), "%P")
errmsg = StringVar()

phone_entry = ttk.Entry(validate="key",validatecommand=check )
phone_entry.pack()

error_label = ttk.Label(textvariable=errmsg, foreground="red")
error_label.pack()

root.mainloop()