#!/usr/local/bin/python3.6
# def set_info(name,age):
#     print("%s is %s years old" % (name,age))
# if __name__ == '__main__':
#     set_info("A",11)
#     set_info("B",age=12)
#     set_info(age=21,name="C")
#     set_info("D",age=24)
# def mytest1(*args):
#     print(args)
# if __name__ == '__main__':
#     mytest1(1)
#
# def mytest2(**kwargs):
#     print(kwargs)
# if __name__ == '__main__':
#     mytest2(name="a",age=12)
def set_info(name,age):
    print("%s is %s years old" % (name,age))
set_info(*("bob",18))
set_info(**{"age":18,"name":"sam"})