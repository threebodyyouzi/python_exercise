# x=10
# def fun1():
#     y="hello"
#     print(y)
#
# def fun2():
#     x="world"
#     print(x)
#
# fun1()
# fun2()
# print(x)
# def fun3():
#     global x
#     x="good"
#     print(x)
# fun3()
# print(x)
# a=range(1,100)
# def fun1():
#     len=1
#     print(len)
# fun1()
# print(len)
from functools import partial
def fun1(a,b,c,d,e,f):
    return a+b+c+d+e+f
print(fun1(1,2,3,4,5,6))
fun2=partial(fun1,1,2,3,4,5)
print(fun2(20))
print(fun2(30))