# div mod calculator v.1.0

from tkinter import *
from tkinter.messagebox import showerror


def next_previous(event):
    global bool_num1
    if bool_num1:
        bool_num1 = False
        input1["borderwidth"] = 0
        input2["borderwidth"] = 1
    else:
        bool_num1 = True
        input1["borderwidth"] = 1
        input2["borderwidth"] = 0


def number_click(num):
    global num1
    global num2
    if bool_num1:
        if num1 != 0:
            num1 = int(str(num1) + str(num))
        else:
            num1 = num
        input1["text"] = str(num1)
    else:
        if num2 != 0:
            num2 = int(str(num2) + str(num))
        else:
            num2 = num
        input2["text"] = str(num2)


def delete():
    global num1
    global num2
    res["text"] = "Результат"
    if bool_num1:
        if len(str(num1)) > 1:
            num1 = int(str(num1)[:-1])
            input1["text"] = str(num1)
        else:
            input1["text"] = "0"
            num1 = 0
    else:
        if len(str(num2)) > 1:
            num2 = int(str(num2)[:-1])
            input2["text"] = str(num2)
        else:
            input2["text"] = "0"
            num2 = 0


def div():
    if num2 == 0:
        showerror(title="Ошибка", message="Деление на 0 невозможно!")
    else:
        res["text"] = str(num1 // num2)


def mod_func():
    if num2 == 0:
        showerror(title="Ошибка", message="Деление на 0 невозможно!")
    else:
        res["text"] = str(num1 % num2)


bool_num1 = True
num1 = 0
num2 = 0

root = Tk()

root.title("DIV MOD Calculator")
root.geometry("400x400+250+50")
root["bg"] = "CadetBlue"

icon = PhotoImage(file="icone.png")
root.iconphoto(False, icon)

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(7): root.rowconfigure(index=r, weight=1)

input1 = Label(text="1 число", background="white", borderwidth=1, relief="solid", font=("Arial", 14), height=2,
               width=10)
input1.grid(row=0, column=0)

nextPrev = Button(text="<->", background="azure2", borderwidth=2, relief="solid", font=("Arial", 10), height=1, width=4)
nextPrev.grid(row=0, column=1)
nextPrev.bind("<Button-1>", next_previous)

input2 = Label(text="2 число", background="white", borderwidth=0, relief="solid", font=("Arial", 14), height=2,
               width=10)
input2.grid(row=0, column=2)

res = Label(text="Результат", background="azure2", font=("Arial", 14), height=2,
            width=20)
res.grid(row=1, column=0, columnspan=3)

div = Button(text="div", background="azure2", borderwidth=2, relief="solid", font=("Arial", 12), height=1, width=4,
             command=div)
div.grid(row=2, column=0)
mod = Button(text="mod", background="azure2", borderwidth=2, relief="solid", font=("Arial", 12), height=1, width=4,
             command=mod_func)
mod.grid(row=2, column=1)
ok = Button(text="delete", background="azure2", borderwidth=2, relief="solid", font=("Arial", 12), height=1, width=6,
            command=delete)
ok.grid(row=2, column=2)

button1 = Button(text="1", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(1))
button1.grid(row=3, column=0)
button2 = Button(text="2", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(2))
button2.grid(row=3, column=1)
# button2.bind(number_click("<Button-1>",2))
button3 = Button(text="3", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(3))
button3.grid(row=3, column=2)
button4 = Button(text="4", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(4))
button4.grid(row=4, column=0)
button5 = Button(text="5", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(5))
button5.grid(row=4, column=1)
button6 = Button(text="6", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(6))
button6.grid(row=4, column=2)
button7 = Button(text="7", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(7))
button7.grid(row=5, column=0)
button8 = Button(text="8", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(8))
button8.grid(row=5, column=1)
button9 = Button(text="9", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(9))
button9.grid(row=5, column=2)
button0 = Button(text="0", background="LightCyan3", borderwidth=2, relief="solid", font=("Arial", 12), height=1,
                 width=4, command=lambda: number_click(0))
button0.grid(row=6, column=1)

root.mainloop()
