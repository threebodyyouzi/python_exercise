# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# import time
# root=Tk()
# root.title("测试用")
# status=StringVar()
# status.set("初始信息")
# status_file=Label(root,textvariable=status)
# status_file.pack()
# root.mainloop()
# for i in range(10):
#     status.set(i)
#     status.get()
#     time.sleep(0.1)
# status.set("failed")
import time
for i in range(20):
    print("\r%s" % ("."*i),end="")
    time.sleep(1)



