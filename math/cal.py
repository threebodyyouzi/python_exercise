#!/usr/local/bin/python3.6
def cal(x,y,z):
    S=(x*y+x*z+y*z)*2
    V=x*y*z
    return (S,V)
if __name__ =="__main__":
    answer=cal(2,3,4)
    print(answer)
