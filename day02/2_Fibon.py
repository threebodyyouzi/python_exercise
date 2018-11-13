#!/usr/local/bin/python3.6
fibon_line=[0,1]

for i in range(2,10):
    tmp=fibon_line[i-2]+fibon_line[i-1]
    fibon_line.append(tmp)
print(fibon_line)
#自选个数的斐波那契数列
fibon_line=[0,1]
num=int(input("请输入数目:"))
for i in range(2,num):
    tmp=fibon_line[i-2]+fibon_line[i-1]
    fibon_line.append(tmp)
print(fibon_line)