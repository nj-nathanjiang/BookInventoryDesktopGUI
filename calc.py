from tkinter import *

window = Tk()


def locate_operation(arg_string: str):
    split_arg_string = arg_string.split(" ")
    return [int(split_arg_string[0]), split_arg_string[1], int(split_arg_string[2])]


def calc():
    t1.delete("1.0", END)
    e1_value_arg = e1_value.get()
    split_up_e1_value = locate_operation(e1_value_arg)
    if not split_up_e1_value:
        t1.insert(END, "Sorry, but I cannot calculate that.")
    elif len(split_up_e1_value) != 3:
        t1.insert(END, "Sorry, but I cannot calculate that.")
    else:
        if split_up_e1_value[1] == "+":
            t1.insert(END, split_up_e1_value[0] + split_up_e1_value[2])
        if split_up_e1_value[1] == "-":
            t1.insert(END, split_up_e1_value[0] - split_up_e1_value[2])
        if split_up_e1_value[1] == "*":
            t1.insert(END, split_up_e1_value[0] * split_up_e1_value[2])
        if split_up_e1_value[1] == "/":
            t1.insert(END, split_up_e1_value[0] / split_up_e1_value[2])


b1 = Button(window, text="Execute", command=calc)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=50)
t1.grid(row=0, column=2)

window.mainloop()
