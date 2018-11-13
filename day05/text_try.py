# try:
#     num=int(input("number: "))
#     result=100 / num
# except (ValueError,ZeroDivisionError):
#     print("Invalid input")
# except (KeyboardInterrupt,EOFError):
#     print("\nBye-bye")
# else:
#     print(result)
# finally:
#     print("done")
def set_age(name,age):
    if not 0<age<150:
        raise ValueError("年龄超出范围")
    print("%s is %d years old" % (name,age))
def set_age2(name,age):
    assert 0<age<150,"断言:年龄超出范围"
    print("%s is %d years old" % (name, age))
if __name__=="__main__":
    set_age("bob",23)
    set_age2("bob",233)