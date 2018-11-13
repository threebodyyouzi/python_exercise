#!/usr/local/bin/python3.6
from random import choice
from string import ascii_letters,digits,punctuation
def passwd(num=8):
    pwd=""
    for time in range(0,num):
        password=choice(ascii_letters+digits+punctuation)
        pwd=pwd+password
    return pwd
if __name__ == "__main__":
    pwd=passwd()
    print(pwd)
