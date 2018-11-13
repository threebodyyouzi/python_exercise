#!/usr/local/bin/python3.6
end_number=int(input("请输入你要查询的范围:2~"))
zhi_number=[]

for number in range(2,end_number):
    for i in range(2,number):
        if number%i==0 :
            break
    else:
        zhi_number.append(number)
print(zhi_number)