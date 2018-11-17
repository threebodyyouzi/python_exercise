#!/usr/local/bin/python3.6
import tkinter
import time
from tkinter.scrolledtext import ScrolledText
from functools import partial
import os
def word_color(color):  #定义修改文字颜色的函数,调用方式:在定义函数前@word_color()
    def set_color(func):
        def red(*word):
            return "\033[31;1m%s\033[0m" % func(*word)
        def green(*word):
            return "\033[32;1m%s\033[0m" % func(*word)
        def yellow(*word):
            return "\033[33;1m%s\033[0m" % func(*word)
        def blue(*word):
            return "\033[34;1m%s\033[0m" % func(*word)
        def purple(*word):
            return "\033[35;1m%s\033[0m" % func(*word)
        colors={"red":red,"green":green,"yellow":yellow,"blue":blue,"purple":purple}
        return colors[color]
    return set_color

@word_color("red")
def error_words(words):
    return "%s" % words
@word_color("yellow")
def warning_words(words):
    return words
@word_color("green")
def success_words(words):
    return "%s" % words
##########################################################################
#############################################################################
def editor():
    root = tkinter.Tk()  # tkinter.Tk(),调用Tk类创建一个实例,这个实例用来充当主窗口的控件
    root.title("我的文本编辑器")
    #############################
    fname=tkinter.Entry()        #在tkinter中，文本框被称为Entry
    fname.pack(side="top", expand=True, fill="x")
    ###########################
    menu=tkinter.Label(root)
    menu.pack(side="top")
    #############################
    status = tkinter.StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
    status.set("这是状态栏")
    status_file=tkinter.Label(root,textvariable=status)
    status_file.pack(expand=True,fill="x")   #expand参数用来打开/关闭fill属性
    ###############################################
    contents = ScrolledText()    #ScrolledText相当于Entry的升级版,这是一个滚动的文本框
    contents.pack(side="bottom",expand=True,fill="both")
#####################################################################################################
    def read_file():
        with open(fname.get()) as fobj:
            contents.delete("1.0", "end")
            contents.insert(tkinter.INSERT, fobj.read())

    def write_file():
        with open(fname.get(),"w") as fobj:
            fobj.write(contents.get("1.0", "end"))


    def create_file():
        if not os.path.exists(fname.get()):
            data=warning_words("路径/文件不存在,即将创建新的路径/文件")
            print(data)
            (path, file) = os.path.split(fname.get())
            try:
                os.makedirs(path)
            except FileExistsError:
                print(warning_words("路径已存在,文件创建中"))
            finally:
                for times in range(20):
                    # line="\r%s%s" % ("@" * times, "." * (9 - times))
                    line="\r%s" % ("."*times)
                    status.set(line)
                    print(line,end="")
                    time.sleep(0.25)
                print()
            with open(fname.get(), "w", encoding='utf-8') as fobj:
                fobj.write("%s" % file)
            data=success_words("路径/文件创建成功")
            status.set(data)
            print(data)
        else:
            print(error_words("路径/文件已存在"))
#############################################################################################################################################
    create_button=tkinter.Button(menu,text="创建",command=create_file)
    create_button.pack(side="left")                                        #side参数定义实例所在的位置,有left,right,bottom,top四个值
    read_button=tkinter.Button(menu,text="打开",command=read_file)
    read_button.pack(side="left")
    write_button=tkinter.Button(menu,text="保存",command=write_file)
    write_button.pack(side="left")
    quit_button=tkinter.Button(menu,text="退出",command=quit)
    quit_button.pack(side="left")


    root.mainloop()
    pass



# @word_color("red")
# def greet():
#     return "Hello world!"
# @word_color("blue")
# def say_hi():
#     return "good_morning"
if __name__ == '__main__':
    # read_file("/tmp/demo/security/passwd")
    editor()
    # create_file("/tmp/a.txt")
    # create_file("/tmp/a1/a2/a3.txt")
    # print([i for i in range(10)])
    # print(warning_words("测试"))
    # exists("/root/c1.txt")
    # print("a"*0)
    # save_file("/root/b.txt")
    # read_file("/root/a.txt")
    # pass
    # print(greet())
    # print(say_hi())
# def create(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         print()
#         pass