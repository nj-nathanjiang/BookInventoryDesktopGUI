from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(column=0, row=0)

l2 = Label(window, text="Author")
l2.grid(column=2, row=0)

l3 = Label(window, text="Year")
l3.grid(column=0, row=1)

title_entry = StringVar()
e1 = Entry(window, textvariable=title_entry)
e1.grid(column=1, row=0)

author_entry = StringVar()
e2 = Entry(window, textvariable=author_entry)
e2.grid(column=3, row=0)

year_entry = StringVar()
e3 = Entry(window, textvariable=year_entry)
e3.grid(column=1, row=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(column=0, row=2, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12)
b1.grid(column=3, row=2)

b2 = Button(window, text="Search entry", width=12)
b2.grid(column=3, row=3)

b3 = Button(window, text="Add entry", width=12)
b3.grid(column=3, row=4)

b4 = Button(window, text="Update", width=12)
b4.grid(column=3, row=5)

b5 = Button(window, text="Delete", width=12)
b5.grid(column=3, row=6)

b6 = Button(window, text="Close", width=12)
b6.grid(column=3, row=7)

window.mainloop()
