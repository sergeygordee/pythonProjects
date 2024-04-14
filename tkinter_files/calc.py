from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalPress():
    global expression
    total = str(eval(expression))
    equation.set(total)

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()


    root.geometry("300x300")

    equation = StringVar()
    expression_field = Entry(root,textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    btn1 = Button(root, text="1", command=lambda:press(1), fg="blue", bg="red", height=1, width=3)
    btn1.grid(row=2,column=0)

    btn2 = Button(root, text="2", command=lambda:press(2), fg="blue", bg="red", height=1, width=3)
    btn2.grid(row=2, column=1)

    btn3 = Button(root, text="3", command=lambda:press(3), fg="blue", bg="red", height=1, width=3)
    btn3.grid(row=2, column=2)

    btn4 = Button(root, text="4", command=lambda:press(4), fg="blue", bg="red", height=1, width=3)
    btn4.grid(row=3, column=0)

    btn5 = Button(root, text="5", command=lambda:press(5), fg="blue", bg="red", height=1, width=3)
    btn5.grid(row=3, column=1)

    btn6 = Button(root, text="6", command=lambda:press(6), fg="blue", bg="red", height=1, width=3)
    btn6.grid(row=3, column=2)

    btn7 = Button(root, text="7", command=lambda:press(7), fg="blue", bg="red", height=1, width=3)
    btn7.grid(row=4, column=0)

    btn8 = Button(root, text="8", command=lambda:press(8), fg="blue", bg="red", height=1, width=3)
    btn8.grid(row=4, column=1)

    btn9 = Button(root, text="9", command=lambda:press(9), fg="blue", bg="red", height=1, width=3)
    btn9.grid(row=4, column=2)

    btn0 = Button(root, text="0", command=lambda:press(0), fg="blue", bg="red", height=1, width=3)
    btn0.grid(row=5, column=1)

    plus = Button(root, text="+", command=lambda:press("+"), fg="blue", bg="red", height=1, width=3)
    plus.grid(row=2,column=3)

    minus = Button(root, text="-", command=lambda:press("-"), fg="blue", bg="red", height=1, width=3)
    minus.grid(row=3, column=3)

    mult = Button(root, text="*", command=lambda:press("*"), fg="blue", bg="red", height=1, width=3)
    mult.grid(row=4, column=3)

    div = Button(root, text="/", command=lambda:press("/"), fg="blue", bg="red", height=1, width=3)
    div.grid(row=5, column=3)

    equal = Button(root, text="=", command=equalPress, fg="blue", bg="red", height=1, width=3)
    equal.grid(row=6, column=3)

    clear = Button(root, text="C", command=clear, fg="blue", bg="red", height=1, width=3)
    clear.grid(row=5, column=2)

    decimal = Button(root, text=".", command=lambda:press("."), fg="blue", bg="red", height=1, width=3)
    decimal.grid(row=5, column=0)

    root.mainloop()