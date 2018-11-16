#!/usr/local/bin/python3.6
#10月14日编写85行
import tkinter
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

def exists(fname):
    if not os.path.exists(fname):
        print(warning_words("路径/文件不存在,即将创建新的路径/文件"))
        (path,file)=os.path.split(fname)
        try:
            os.makedirs(path)
        except FileExistsError:
            print(warning_words("路径已存在,文件创建中"))
        with open(fname,"w",encoding='utf-8') as fobj:
            fobj.write("%s" % file)
        print(success_words("路径/文件创建成功"))
    else:
        print(error_words("路径/文件已存在"))

def read_file(fname):
    with open(fname) as fobj:
        print(fobj.read())

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





# @word_color("red")
# def greet():
#     return "Hello world!"
# @word_color("blue")
# def say_hi():
#     return "good_morning"
if __name__ == '__main__':
    # print(warning_words("测试"))
    # exists("/root/a.txt")
    save_file("/root/a.txt")
    read_file("/root/a.txt")
    # pass
    # print(greet())
    # print(say_hi())
# def create(path):
#     if not os.path.exists(path):
#         os.makedirs(path)
#         print()
#         pass