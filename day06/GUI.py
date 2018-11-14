import tkinter
from functools import partial
root = tkinter.Tk()
lb=tkinter.Label(text="Hello World")
b1=tkinter.Button(root,fg="white",bg="blue",text="Button 1")
Mybutton=partial(tkinter.Button,root,fg="white",bg="blue")
b2=Mybutton(text="Button 2")
b3=Mybutton(text="quit",command=quit)
for item in [lb,b1,b2,b3]:
    item.pack()
root.mainloop()