from tkinter import *
import runpy


def choice_1():
    file_globals = runpy.run_path("Choice_1.py")


def choice_2():
    file_globals = runpy.run_path("Choice_2.py")


def choice_3():
    file_globals = runpy.run_path("Choice_3.py")


def choice_4():
    file_globals = runpy.run_path("Choice_4.py")


def choice_5():
    file_globals = runpy.run_path("Choice_5.py")


def choice_6():
    file_globals = runpy.run_path("Choice_6.py")


def choice_7():
    file_globals = runpy.run_path("Choice_7.py")


root = Tk()
root.title("F&B RECOMMENDATION SYSTEM")
root.geometry("500x600")
frame_in = Frame(root)
frame_in.pack(anchor=CENTER)

button_1 = Button(frame_in, text='Sort by Distance', command=choice_1, height=3, width=20).grid(row=0)
button_2 = Button(frame_in, text='Check by Price', command=choice_2, height=4, width=20).grid(row=1)
button_3 = Button(frame_in, text='Rate and Rank List', command=choice_3, height=4, width=20).grid(row=2)
button_4 = Button(frame_in, text='Search by Food', command=choice_4, height=4, width=20).grid(row=3)
button_5 = Button(frame_in, text='Update Info', command=choice_5, height=4, width=20).grid(row=4)
button_6 = Button(frame_in, text='Detail about Canteens', command=choice_6, height=4, width=20).grid(row=5)
button_7 = Button(frame_in, text='Display the map', command=choice_7, height=4, width=20).grid(row=6)
button_8 = Button(frame_in, text='Quit', command=root.destroy, height=4, width=20).grid(row=7)

root.mainloop()
