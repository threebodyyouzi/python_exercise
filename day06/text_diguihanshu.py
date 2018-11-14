#!/usr/local/bin/python3.6
def fun1(x):
    if x==1:
        return 1
    return fun1(x-1)*x
print(fun1(20))
print(fun1(12))