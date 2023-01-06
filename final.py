from tkinter import *
from tkinter.messagebox import *
import time;
root=Tk()
icon1=PhotoImage(file="")
root.geometry('1400x1400')
root.title('Splash Screen')
l=Label(root,image=icon1)
l.grid(row=0,column=0)
l5=Label(root,text='Name:-RAVI SHANKAR ',font='Arial 12 underline')
l5.grid(row=1,column=0)                
l1=Label(root,text='Enrollment number:- LNCBMCAAI072',font='Arial 12 underline')
l1.grid(row=2,column=0)
l2=Label(root,text='MCA-AIML',font='Arial 12 underline')
l2.grid(row=3,column=0)
l3=Label(root,text='Email:-dprajapati389@gmail.com',font='Arial 12 underline')
l3.grid(row=4,column=0)
l4=Label(root,text='Mobile:-8381983312',font='Arial 12 underline')
l4.grid(row=5,column=0)
def fun(e):
    root.destroy()
    import showbook
l.bind('<Motion>',fun)
l1.bind('<Motion>',fun)
l2.bind('<Motion>',fun)
l3.bind('<Motion>',fun)
l4.bind('<Motion>',fun)
l5.bind('<Motion>',fun)
root.mainloop()

