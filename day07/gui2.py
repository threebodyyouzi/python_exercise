# from tkinter import *
#
#
# def p_label():
#     global root
#     Lb = Label(root, text='我爱python')
#     Lb.pack()
#
#
# root = Tk()
# B_n = Button(root, text='点我', command=p_label)  # command后面不能有任何的标点符号
# B_n.pack()
# root.mainloop()
from tkinter import *
from tkinter.scrolledtext import ScrolledText
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)
Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)
mainloop()