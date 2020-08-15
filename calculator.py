from tkinter import*

root=Tk()
root.title('calculator')

e=Entry(root,width=40,borderwidth=10,fg='white',bg='green')
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
def button_click(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,cur+str(number))
def button_add():
    num_1=e.get()
    global num
    global operation
    operation= "add"
    num=int(num_1)
    e.delete(0,END)

def button_clear():
    e.delete(0,END)

def button_equal():   
     num_2=e.get()
     e.delete(0,END)
     if operation=='add':
         e.insert(0,num  + int(num_2))
     if operation=='sub':
         e.insert(0,num -int(num_2))
     if operation=='mul':
        e.insert(0,num  * int(num_2))
     if operation=='div':
        e.insert(0,num  / int(num_2))
def button_subtract():
    num_1=e.get()
    global num
    global operation
    operation= "sub"
    num=int(num_1)
    e.delete(0,END)


def button_multiply():
      num_1=e.get()
      global num
      global operation
      operation= "mul"
      num=int(num_1)
      e.delete(0,END)

def button_divide():
    num_1=e.get()
    global num
    global operation
    operation= "div"
    num=int(num_1)
    e.delete(0,END)









  

button_1=Button(root, text='1',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command=lambda: button_click(1))
button_2=Button(root, text='2',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(2))
button_3=Button(root, text='3',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command=lambda: button_click(3))
button_4=Button(root, text='4',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(4))
button_5=Button(root, text='5',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(5))
button_6=Button(root, text='6',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(6))
button_7=Button(root, text='7',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(7))
button_8=Button(root, text='8',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(8))
button_9=Button(root, text='9',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= lambda:button_click(9))
button_0=Button(root, text='0',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command=lambda: button_click(0))


button_add=Button(root, text='+',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= button_add)
button_clear=Button(root, text='clear',padx=80,pady=20,fg='black',bg='green',borderwidth=5,command= button_clear)
button_equal=Button(root, text='=',padx=80,pady=20,fg='black',bg='green',borderwidth=5,command= button_equal)

button_subtract=Button(root, text='-',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= button_subtract)
button_multiply=Button(root, text='*',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= button_multiply)
button_divide=Button(root, text='/',padx=40,pady=20,fg='black',bg='green',borderwidth=5,command= button_divide)

button_1.grid(row=3 ,column=0 )
button_2.grid(row= 3,column= 1)
button_3.grid(row= 3,column=2)

button_4.grid(row=2 ,column=0 )
button_5.grid(row=2 ,column= 1)
button_6.grid(row= 2,column= 2)

button_7.grid(row=1 ,column=0)
button_8.grid(row= 1,column=1 )
button_9.grid(row=1 ,column=2 )

button_0.grid(row=4 ,column=0 )



button_add.grid(row= 1,column=4 )
button_clear.grid(row=4 ,column=1,columnspan=2 )
button_equal.grid(row=5 ,column=1 ,columnspan=2)

button_subtract.grid(row= 2,column=4 )
button_multiply.grid(row= 3,column=4)
button_divide.grid(row= 4,column=4)




root.mainloop()
