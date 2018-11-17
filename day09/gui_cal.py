from tkinter import *
import math
#----------------------------
root=Tk()
root.minsize(300,500)
root.title("我的计算器")
#------------------------------
screen=StringVar()
screen.set(0)
#------------------------------
numberlist=[]
judge=False
#------------------------------
def buttons(num):
	global judge
	if judge==True:      #判断是否存在运算符，若存在，则将前一个数字存入列表，再将输入的数字显示在屏幕上
		screen.set(0)
		judge=False
	prenumber=screen.get()
	if prenumber=="0":
		screen.set(num)
	else:
		if num=="+/-":
			if prenumber.startswith("-"):
				screen.set(prenumber[1:])
			else:
				screen.set("-"+prenumber)
		else:
			screen.set(prenumber+num)
#------------------------------------------------------------------------------
#定义数字的符号，决定是正数还是负数
def signbutton(button):
	global numberlist
	global judge
	prenumber=screen.get()
	numberlist.append(prenumber)
	numberlist.append(button)
	judge=True
#-------------------------------------------------------
#定义了三个等式，等号、求根、求倒数
def equalbutton(button):
	global numberlist
	if button=="=":
		prenumber=screen.get()
		numberlist.append(prenumber)
		print(numberlist)
		result="".join(numberlist)
		answer=eval(result)
		print(answer)
		screen.set(answer)
		numberlist.clear()
	if button=='√':
		prenumber=screen.get()
		answer=math.sqrt(float(prenumber))
		print(answer)
		screen.set(answer)
	if button=="1/x":
		prenumber=screen.get()
		answer=1/float(prenumber)
		print(answer)
		screen.set(answer)
#-------------------------------------------------------------------------------
def calbutton(button):
	global numberlist
	global judge
	prenumber=screen.get()
	numberlist.append(prenumber)
	numberlist.append(button)
	judge=True
	print(numberlist)
#------------------------------------------------------------
def clear():
	global numberlist
	global judge
	numberlist.clear()
	judge=False
	screen.set(0)
#---------------------------------------------------------
#文本框
label=Label(root,textvariable=screen,bg="gray")
label.pack(side="top",expand=True,fill="x")
#--------------------------------------------------------
label2=Label(root)
label2.pack(expand=True,fill="x")
button1_1=Button(label2,text="C",command=lambda:clear())
button1_1.pack(side="left",expand=True,fill="y")
button1_2=Button(label2,text="√",command=lambda:equalbutton("√"))
button1_2.pack(side="left",expand=True,fill="y")
button1_3=Button(label2,text="1/x",command=lambda:equalbutton("1/x"))
button1_3.pack(side="left",expand=True,fill="y")
button1_4=Button(label2,text="÷",command=lambda:calbutton("/"))
button1_4.pack(side="left",expand=True,fill="y")
#---------------------------------------------------------------
label3=Label(root)
label3.pack(expand=True,fill="x")
button2_1=Button(label3,text="7",command=lambda:buttons("7"))
button2_1.pack(side="left",expand=True,fill="y")
button2_2=Button(label3,text="8",command=lambda:buttons("8"))
button2_2.pack(side="left",expand=True,fill="y")
button2_3=Button(label3,text="9",command=lambda:buttons("9"))
button2_3.pack(side="left",expand=True,fill="y")
button2_4=Button(label3,text="×",command=lambda:calbutton("*"))
button2_4.pack(side="left",expand=True,fill="y")
#-------------------------------------------------------------------
label4=Label(root)
label4.pack(expand=True,fill="x")
button3_1=Button(label4,text="4",command=lambda:buttons("4"))
button3_1.pack(side="left",expand=True,fill="y")
button3_2=Button(label4,text="5",command=lambda:buttons("5"))
button3_2.pack(side="left",expand=True,fill="y")
button3_3=Button(label4,text="6",command=lambda:buttons("6"))
button3_3.pack(side="left",expand=True,fill="y")
button3_4=Button(label4,text="-",command=lambda:calbutton("-"))
button3_4.pack(side="left",expand=True,fill="y")
#-------------------------------------------------------------------
label5=Label(root)
label5.pack(expand=True,fill="x")
button4_1=Button(label5,text="1",command=lambda:buttons("1"))
button4_1.pack(side="left",expand=True,fill="y")
button4_2=Button(label5,text="2",command=lambda:buttons("2"))
button4_2.pack(side="left",expand=True,fill="y")
button4_3=Button(label5,text="3",command=lambda:buttons("3"))
button4_3.pack(side="left",expand=True,fill="y")
button4_4=Button(label5,text="+",command=lambda:calbutton("+"))
button4_4.pack(side="left",expand=True,fill="y")
#---------------------------------------------------------------------
label6=Label(root)
label6.pack(expand=True,fill="x")
button5_1=Button(label6,text="+/-",command=lambda:signbutton("+/-"))
button5_1.pack(side="left",expand=True,fill="y")
button5_2=Button(label6,text="0",command=lambda:buttons("0"))
button5_2.pack(side="left",expand=True,fill="y")
button5_3=Button(label6,text=".",command=lambda:buttons("."))
button5_3.pack(side="left",expand=True,fill="y")
button5_4=Button(label6,text="=",command=lambda:equalbutton("="))
button5_4.pack(side="left",expand=True,fill="y")
#---------------------------------------------------------------------
mainloop()