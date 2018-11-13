#!/usr/local/bin/python3.6
# def foo():
#     print("The World!")
#
# foo()
# print(foo)
def fib(num):
    fibs=[0,1]
    for i in range(num-2):
        fibs.append(fibs[-1]+fibs[-2])
    print(fibs)

if __name__ == "__main__":
    fib(5)
    fib(10)
    fib(20)