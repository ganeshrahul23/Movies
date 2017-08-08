import os
from tkinter import *
import xlsxwriter

top = Tk()

def Pressed1():   
        mypath = os.getcwd()
        year = os.listdir(mypath)
        year_size = len(year)
        temp = [] #Empty list
        for i in range(0,year_size):
                        year_path = mypath + '\\' + year[i]
                        if os.path.isdir(year_path):
                            movies = os.listdir(year_path)
                            tmov_size = len(movies)
                            y = 0;
                            for x in movies:
                                movies[y] = x + "!*" + year[i]
                                y = y + 1
                            movies = movies + temp
                            temp = movies       
        movies.sort()
        mov_siz = len(movies)
        wid = len(max(movies,key = len))

        #==========To create a excel file==========#
        workbook = xlsxwriter.Workbook('Movies.xlsx')
        MovDB = workbook.add_worksheet()
        MovDB.set_column('C:C', wid)
        bold = workbook.add_format({'bold': True})
        MovDB.write(0,0,'No.',bold)
        MovDB.write(0,1,'Year',bold)
        MovDB.write(0,2,'Title',bold)
        row = 1
        for i in range(0,mov_siz):
                        MovDB.write(row,0,i+1)
                        movi,sep,yea = movies[i].partition('!*')
                        MovDB.write(row,1,yea)
                        MovDB.write(row,2,movi)
                        row = row + 1
        workbook.close()
        #==========================================#
def Pressed2():
        os.system("start "+"Movies.xlsx")
        
button1 = Button(top,text="Update Database",justify=CENTER,fg="red",command=Pressed1)
button1.pack()

button2 = Button(top,text="Open Database",justify=CENTER,fg="blue",command=Pressed2)
button2.pack()

top.mainloop()
