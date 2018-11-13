#!/usr/local/bin/python3.6
grade=int(input("输入你的成绩:"))

if grade>=90:
    print("优秀")
elif grade>=80:
    print("良")
elif grade>=70:
    print("好")
elif grade>=60:
    print("合格")
else:
    print("准备留级吧")