#!/usr/local/bin/python3.6
import random
_answer=random.randint(1,100)
_count=5
i=0

while i < _count:
    _guess=int(input("请输入猜的数字:"))
    if _guess < 1 or _guess > 100 :
        print("超出范围")
    elif _guess < _answer :
        print("猜小了")
    elif _guess > _answer :
        print("猜大了")
    else :
        print("猜对了")
        break
    i+=1
else :
    print("答案是"+str(_answer))
