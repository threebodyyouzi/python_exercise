#!/usr/local/bin/python3.6
from string import ascii_letters,digits,punctuation
from random import choice
all_choice = digits + ascii_letters + punctuation

def randpass(n=8):
     result=[choice(all_choice) for i in range(n)]
     return "".join(result)

if __name__ == '__main__':
    print(randpass())
    print(randpass(10))