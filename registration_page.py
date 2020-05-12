"""
PYTHON TUTORIALS
REGISTRATION PAGE
PART - I
create table register(name varchar(100),username varchar(100) primary key, email varchar(100),password varchar(100));
"""

from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

mycon = sql.connect(host = 'localhost',user = 'root',passwd = 'root',database = 'test')
cur = mycon.cursor()


root = Tk()
def submit(event):
    name = t1.get()
    user_name = t2.get()
    new_email = t3.get()
    passwd = t4.get()
    cpasswd = t5.get()
    if name and user_name and new_email and passwd and cpasswd:
        cur.execute('select username,email from register')
        total= cur.fetchall()
        username = []
        exist_email = []
        for i in total:
            username.append(i[0])
            exist_email.append(i[1])
        
        if new_email in exist_email:
            messagebox.showinfo('ALERT!','Email Alreay Exists')
            e3.delete(0,END)
        else:
            if user_name in username:
                messagebox.showinfo('ALERT!','Username Alreay Exists')
                e2.delete(0,END)
            else:
                if passwd != cpasswd:
                    messagebox.showinfo('ALERT!','Password do not match')
                    e4.delete(0,END)
                    e5.delete(0,END)
                else:
                    exe = f'insert into register values("{name}","{user_name}","{new_email}","{passwd}")'
                    cur.execute(exe)
                    mycon.commit()
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e5.delete(0,END)
                    messagebox.showinfo('SUCCESS','REGISTRATION SUCCESSFUL!')
    else:
        messagebox.showinfo('ALERT!','ALL FIELDS MUST BE FILLED')
                    

root.geometry('700x500')
root.resizable(0,0)
root.wm_iconbitmap('icon.ico')
root.title('REGISTRATION PAGE')
root.configure(bg = '#D3D3D3')

# LABEL
l0 = Label(root,text = 'REGISTRATION\nPAGE',font = ('normal',25,'bold'),bg = '#D3D3D3')
l0.place(x = 220, y = 60)


l1 = Label(root,text = 'NAME',font = ('arial',15,'normal'),bg = '#D3D3D3')
l1.place(x = 205, y = 160)

l2 = Label(root,text = 'USER NAME',font = ('arial',15,'normal'),bg = '#D3D3D3')
l2.place(x = 150, y = 195)

l3 = Label(root,text = 'EMAIL',font = ('arial',15,'normal'),bg = '#D3D3D3')
l3.place(x = 205, y = 230)

l4 = Label(root,text = 'PASSWORD',font = ('arial',15,'normal'),bg = '#D3D3D3')
l4.place(x = 150, y = 265)

l0 = Label(root,text = 'CONFIRM PASSWORD',font = ('arial',15,'normal'),bg = '#D3D3D3')
l0.place(x = 55, y = 300)


# ENTRY
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
e1 = Entry(root,width = 20,font = ('normal',15),bd = 3,textvariable = t1)
e1.place(x = 300 , y = 160)

e2 = Entry(root,width = 20,font = ('normal',15),bd = 3,textvariable = t2)
e2.place(x = 300 , y = 195)

e3 = Entry(root,width = 20,font = ('normal',15),bd = 3,textvariable = t3)
e3.place(x = 300 , y = 230)

e4 = Entry(root,width = 20,font = ('normal',15),bd = 3,textvariable = t4,show = '*')
e4.place(x = 300 , y = 265)

e5 = Entry(root,width = 20,font = ('normal',15),bd = 3,textvariable = t5,show = '*')
e5.place(x = 300 , y = 300)

b1 = Button(root, text = 'SUBMIT',font = ('normal',15),bd = 3, command = lambda: submit(None))
b1.place(x = 330 , y = 350)
def w1(event):
    e2.focus()

def w2(event):
    e3.focus()

def w3(event):
    e4.focus()

def w4(event):
    e5.focus()

e1.bind('<Return>',w1)
e2.bind('<Return>',w2)
e3.bind('<Return>',w3)
e4.bind('<Return>',w4)
e5.bind('<Return>',submit)
root.mainloop()
