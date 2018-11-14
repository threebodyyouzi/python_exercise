# a=lambda x,y:(x+y)
# print(a(1,2))
from random import randint
# def fun1(x):
#     return x>50
# a1=[randint(1,100) for i in range(10)]
# a2=[randint(1,100) for i in range(10)]
# print(a1)
# print(a2)
# print(list(filter(fun1,a1)))
#
# b=filter(lambda x:x%2,a1)
# print(list(b))
def func2(x):
    return x*x+2
a=[randint(1,100) for i in range(10)]
print(list(map(func2,a)))
print(list(map(lambda x:x*x-2,a)))