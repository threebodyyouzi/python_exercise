import datetime
# class A:
#     def foo(self):
#         print("你好")
#     def pstar(self):
#         print("*"*50)
# class B:
#     def bar(self):
#         print("世界")
#     def pstar(self):
#         print("#"*50)
#
# class C(A,B):
#     pass
# class D(B,A):
#     pass
#
# if __name__ == '__main__':
#     c=C()
#     d=D()
#     c.pstar()
#     d.pstar()
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#
#     def __str__(self):
#         return "<<%s>>" % self.title
#
#     def __call__(self):
#         print("<<%s>> is written by %s " % (self.title,self.author))
#
# if __name__ == '__main__':
#     core=Book("als","aaa")
#     print(core)
#     core()
class Myclass():
    def hello(self):
        print("Hello")

    @staticmethod
    def welcome():
        print("你好")
    @classmethod
    def greet(cls):
        print("???")
if __name__ == '__main__':
    Myclass.welcome()
    Myclass.hello(1)
    Myclass.greet()