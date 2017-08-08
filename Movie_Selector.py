from tkinter import *
import os
import random

top = Tk()
top.maxsize(400,100);
top.minsize(400,100);
w1 = Label(top)
w1.grid(row = 0, column = 1)
w2 = Label(top)
w2.grid(row = 1, column = 1)

def Pressed():
         global w1
         global w2
         w1.grid_forget()
         w2.grid_forget()
         
         mypath=os.getcwd()
         folders = os.listdir(mypath)

         t_flag = False
         while not t_flag:
            year = random.choice(folders)
            year_path = mypath + '\\' + year
            t_flag = os.path.isdir(year_path)
         txt1 = "Year : " + year
         
         w1 = Label(top,justify=CENTER,text=txt1)
         w1.grid(row = 0, column = 1)
         
         mypath = mypath + '\\' + year
         folders = os.listdir(mypath)
         movie = random.choice(folders)
         txt2 = "Movie : " + movie
         
         w2 = Label(top,justify=CENTER,text=txt2,anchor=W)
         w2.grid(row = 1, column = 1)

button = Button(top,text="Generate",justify=CENTER,fg="red",command=Pressed)
button.config( height = 2, width = 15 )
button.grid(row = 0, column = 0,sticky=N+E+S+W)
top.mainloop()
