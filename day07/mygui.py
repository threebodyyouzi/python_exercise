#!/usr/local/bin/python3.6
#10月14日编写85行
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



def create_file(fname):
    if not os.path.exists(fname):
        print(warning_words("路径/文件不存在,即将创建新的路径/文件"))
        (path,file)=os.path.split(fname)
        try:
            os.makedirs(path)
        except FileExistsError:
            print(warning_words("路径已存在,文件创建中"))
        finally:
            for times in range(10):
                print("\r%s%s" % ("@"*times,"."*(9-times)),end="")
                time.sleep(0.25)
            print()
        with open(fname,"w",encoding='utf-8') as fobj:
            fobj.write("%s" % file)
        print(success_words("路径/文件创建成功"))
    else:
        print(error_words("路径/文件已存在"))

def read_file(fname):
    # with open(fname) as fobj:
    #     data=fobj.read()
    #     print(data)
    with open(fname) as fobj:
        contents.delete("1.0",END)
        contents.insert(INSERT,fobj.read())

def write_data():
    data=[]
    print('''请输入文本内容,输入EOF退出编辑''')
    while True:
        word=input('''>''')
        if word == "EOF":
            break
        data.append(word+"\n")
    data="".join(data)
    # print(type(data))
    return data

def save_file(fname):
    with open(fname,"a") as fobj:
        data=write_data()
        fobj.write(data)
    with open(fname,"r") as fobj:
        print(fobj.read())


def editor(fname):
    top=tkinter.Tk()         #tkinter.Tk(),创建一个充当主窗口的控件
    top.title("我的文本编辑器")
    lb=tkinter.Label(text="New file")
    # read_button=tkinter.Button(top)#创建一个按钮,还有种设置方式,read_button.config(text="",command=)
    # read_button["text"]="读取文件"
    # read_button["command"]=read_file(fname)
    read_button=tkinter.Button(top,text="load",command=read_file())
    write_button=tkinter.Button(top,text="编辑",command=save_file())
    quit_button=tkinter.Button(top,text="退出",command=quit)
    for item in [lb,read_button,write_button,quit_button]:
        item.pack(side="left")
    global contents
    contents = ScrolledText()
    contents.pack(side="BOTTOM",expand=True,fill="BOTH")
    # contents=tkinter.ScrolledText()
    # contents.pack()
    top.mainloop()
    pass



# @word_color("red")
# def greet():
#     return "Hello world!"
# @word_color("blue")
# def say_hi():
#     return "good_morning"
if __name__ == '__main__':
    # read_file("/tmp/demo/security/passwd")
    editor("/tmp/demo/security/passwd")
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