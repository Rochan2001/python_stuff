import MySQLdb
from tkinter import *
root = Tk()
def retrieve_rows(eno):
    conn = MySQLdb.connect(host="localhost",database="world",user="root",password="Rocky@999999")
    cursor = conn.cursor()
    str = "select * from emptab where eno = '%d'"
    args = (eno)
    cursor.execute(str % args)
    row = cursor.fetchone()
    if row is not None:
        lbl = Label(text = row,font=('Arial',14)).place(x=50,y=200)
    cursor.close()
    conn.close()
def display(self):
    str = e1.get()
    lbl = Label(text="you entered: "+str,font=('Arial',14)).place(x=50,y=150)
    retrieve_rows(int(str))
f = Frame(root,height= 350,width = 600)
f.propagate(0)
f.pack()
l1 = Label(text="Enter employee number :",font=('Arial',14))
e1 = Entry(f,width = 15,fg='blue',bg='yellow',font=('Arial',14))
e1.bind("<Return>",display)
l1.place(x=50,y=100)
e1.place(x=300,y=100)
root.mainloop()