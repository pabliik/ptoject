from tkinter import *

def print_hello():
    print("Hello" * 5)

print("Hello1" * 5)

win = Tk()

button = Button(win, text="Hello", command=print_hello)
# button = Button(win, text="Hello", command=lambda: print_hello(5))



button.pack()


win.mainloop()