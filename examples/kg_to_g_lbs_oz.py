# My Kg to G, Lbs, and Oz Converter

from tkinter import *

window = Tk()


def convert_kg_to_g_lbs_oz():
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    try:
        t1.insert(END, round(float(e1_value.get()) * 1000, 2))
    except ValueError:
        t1.insert(END, "You did not enter a float.")

    try:
        t2.insert(END, round(float(e1_value.get()) * 2.20462, 2))
    except ValueError:
        t2.insert(END, "You did not enter a float.")

    try:
        t3.insert(END, round(float(e1_value.get()) * 35.274, 2))
    except ValueError:
        t3.insert(END, "You did not enter a float.")


kg_l = Label(window, text="Kg:")
kg_l.grid(column=0, row=0, columnspan=2, rowspan=1, sticky="EW")

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(column=2, row=0, columnspan=2, rowspan=1, sticky="EW")

b1 = Button(window, text="Convert", command=convert_kg_to_g_lbs_oz)
b1.grid(column=4, row=0, columnspan=2, rowspan=1, sticky="EW")

t1 = Text(window, height=1, width=10)
t1.grid(column=0, row=1)

l1 = Label(window, text="grams")
l1.grid(column=1, row=1)

t2 = Text(window, height=1, width=10)
t2.grid(column=2, row=1)

l2 = Label(window, text="pounds")
l2.grid(column=3, row=1)

t3 = Text(window, height=1, width=10)
t3.grid(column=4, row=1)

l3 = Label(window, text="ounces")
l3.grid(column=5, row=1)

window.mainloop()
