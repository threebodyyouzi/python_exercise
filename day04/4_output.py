#!/usr/local/bin/python3.6
content=[]
print("请输入单词,输入EOF退出")
while True:
    word=input(">")
    if word=="EOF":
        break
    content.append(word)
print("+"+"*"*48+"+")
for word in content:
    print("+"+"{:^48}".format(word)+"+")
print("+"+"*"*48+"+")