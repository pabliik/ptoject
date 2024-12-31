from tkinter import *

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

lb2 = Listbox(top)
lb2.insert(1, "Python")
lb2.insert(2, "Perl")
lb2.insert(3, "C")
lb2.insert(4, "PHP")
lb2.insert(5, "JSP")
lb2.insert(6, "Ruby")

Lb1.pack()

lb2.pack()
top.mainloop()