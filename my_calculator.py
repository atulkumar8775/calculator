import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("Calculator")

Cal_F = Frame(root,bg = 'Powder Blue',bd=6,relief =RIDGE)
Cal_F.pack(side = TOP)


Cal_L = Frame(root,bg = 'Powder Blue',bd=6,relief =RIDGE)
Cal_L.pack(side = BOTTOM)

text_input = StringVar()
operator = ''

txtDisplay = Entry(Cal_F,width =20,bg="white",bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_input)
txtDisplay.grid(row=0,column=0,columnspan =4,pady=1)
txtDisplay.insert(0,'0')


lable= Label(Cal_L,width = 28,padx=16,pady=1,bd=3,fg="black",font =('arial',16,'bold'),text='Developed By Atul Kumar',bg="powder blue").grid(row=6,column=0)




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ''
    text_input.set('')


def btnEquals():
    global operator
    add = str(eval(operator))
    text_input.set(add)
    operator = ""


#**************************Calculator Button************************

btn7 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='7',bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='8',bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='9',bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)

btnAdd = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='+',bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)

#**************************

btn4 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='4',command=lambda:btnClick(4)).grid(row=3,column=0)

btn5 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='5',command=lambda:btnClick(5)).grid(row=3,column=1)

btn6 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='6',command=lambda:btnClick(6)).grid(row=3,column=2)

btnSub = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='-',bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)
#**********************

btn1 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='1',command=lambda:btnClick(1)).grid(row=4,column=0)

btn2 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='2',command=lambda:btnClick(2)).grid(row=4,column=1)

btn3 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='3',command=lambda:btnClick(3)).grid(row=4,column=2)

btnmult= Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='*',bg="powder blue",command=lambda:btnClick('*')).grid(row=4,column=3)
#*********************

btn0 = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='0',bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='Clear',bg="powder blue",command = btnClear).grid(row=5,column=1)

btnEqual = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='=',bg="powder blue",command = btnEquals).grid(row=5,column=2)

btnDiv = Button(Cal_F,padx=16,pady=1,bd=7,fg="black",font =('arial',16,'bold'),width=4,
                  text='/',bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)







root.mainloop()