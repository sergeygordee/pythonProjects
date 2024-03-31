import tkinter
from tkinter import *
from tkinter import ttk

'''
добавить возможность сохранения количества кликов
 внутрь файла
и считывать эти данные о кликах в программу
'''
clicks = 0


def click_button():
    global clicks
    clicks += 100
    btn["text"] = f"Clicks {clicks}"


root = tkinter.Tk()
root.title("Бравл старс")
root.geometry("300x300")
icon = PhotoImage(file="qwe.png")
root.iconphoto(False, icon)
# btn = ttk.Button(text="Нажми", command=click_button)
# btn.pack(anchor ="nw", padx=20,pady=20,fill=X)

btn1 = ttk.Button(text="Bottom")
btn1.pack(side=BOTTOM)

btn2 = ttk.Button(text="Right")
btn2.pack(side=RIGHT)

btn3 = ttk.Button(text="Left")
btn3.pack(side=LEFT)

btn4 = ttk.Button(text="Top")
btn4.pack(side=TOP)

btn5 = ttk.Button(text="btn")
btn5.place(x=130,y=20, width=80,height=50)
root.mainloop()
