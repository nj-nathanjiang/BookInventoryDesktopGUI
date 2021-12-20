from tkinter import *

window = Tk()


def convert_km_mile():
    t1.delete("1.0", END)
    try:
        t1.insert(END, round(float(e1_value.get()) / 1.609, 2))
    except ValueError:
        t1.insert(END, "You did not enter a float.")


b1 = Button(window, text="Execute", command=convert_km_mile)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=30)
t1.grid(row=0, column=2)

window.mainloop()
