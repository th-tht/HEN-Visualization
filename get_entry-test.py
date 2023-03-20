from tkinter import *
import tkinter as tk
def get():
    print("获取到的内容是 %s" % entry.get()) #\033[91m
 
root=tk.Tk()
root.title('获取Entry内容')
root.geometry('200x100')
 
frame = Frame(root)
frame.pack()
u1 = tk.StringVar()
entry = tk.Entry(frame, width=20, textvariable=u1)
entry.pack(side="left")
 
frame1 = Frame(root)
frame1.pack()
btn1=Button(frame1, text="获取", width=20, height=1, command=lambda:get())
btn1.pack(side="left")
 
root.mainloop()