from tkinter import *


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0


sum1 = Calc()
root = Tk()
calc = Frame(root, bg = "light grey")
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT, bd=1, insertwidth=1, font=40, fg="black", bg="light green")
text_box.grid(row = 0, column = 0, columnspan = 7)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
button = []
for j in range(1,4):
    for k in range(3):
        button.append(Button(calc, text = numbers[i], width=1, padx=16, pady=16, bd=8, fg = "black"))
        button[i].grid(row = j, column = k, pady = 10, padx=5)
        button[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1
dot = Button(calc, text = ".", width=1, padx=16, pady=16, bd=8, fg = "black", bg = "light blue")
dot["command"] = lambda: sum1.num_press(".")
dot.grid(row = 1, column = 5, pady = 5)

all_clear = Button(calc, text = "AC", width=1, padx=16, pady=16, bd=8, bg="red", fg = "black")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 4, column = 0, pady = 5)

surd = Button(calc, text = "√", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
surd["command"]
surd.grid(row = 1, column = 6, pady = 5)

button0 = Button(calc,width=1, padx=16, pady=16, bd=8, text="0", fg = "black")
button0["command"] = lambda: sum1.num_press(0)
button0.grid(row = 4, column = 1, pady = 5)

clear = Button(calc, text = "C", width=1, padx=16, pady=16, bd=8, bg="green", fg = "black")
clear["command"] = sum1.cancel
clear.grid(row = 4, column = 2, pady = 5)

divide = Button(calc, text = "÷", width=1, padx=16, pady=16, bd=8, fg = "black", bg = "light blue")
divide["command"] = lambda: sum1.operation("divide")
divide.grid(row = 1, column = 3, pady = 5)

buttonTimes = Button(calc, text = "X",  width=1, padx=16, pady=16, bd=8, fg = "black",bg = "light blue")
buttonTimes["command"] = lambda: sum1.operation("times")
buttonTimes.grid(row = 2, column = 3)

minus = Button(calc, text = "-", width=1, padx=16, pady=16, bd=8, fg = "black", bg = "light blue")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = 5)

add = Button(calc, text = "+", width=1, padx=16, pady=16, bd=8, fg = "black", bg = "light blue")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = 5)

equals = Button(calc, text = "=", width=1, padx=75, pady=16, bd=8, bg="yellow", fg = "black")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5, columnspan = 7)

sin = Button(calc, text = "SIN", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
sin["command"]
sin.grid(row = 2, column = 5, pady = 5)

Asin = Button(calc, text = "ASIN", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
Asin["command"]
Asin.grid(row = 2, column = 6, pady = 5)

cos = Button(calc, text = "COS", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
cos["command"]
cos.grid(row = 3, column = 5, pady = 5)

Acos = Button(calc, text = "ACOS", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
Acos["command"]
Acos.grid(row = 3, column = 6, pady = 5)

tan = Button(calc, text = "TAN", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
tan["command"]
tan.grid(row = 4, column = 5, pady = 5)

Atan = Button(calc, text = "ATAN", width=1, padx=16, pady=16, bd=8, bg="light blue", fg = "black")
Atan["command"]
Atan.grid(row = 4, column = 6, pady = 5)

root.mainloop()
