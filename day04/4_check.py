#!/usr/local/bin/python3.6
import keyword
from string import ascii_letters,digits,punctuation
#i=0

print("请输入待查字符")
words=input(">")
def keycheck():
    if keyword.iskeyword(words):
        print("%s是关键词" % words)
    #    i+=1
    else:
        print("%s不是关键词" % words)
def wordcheck():
    m=0
    for key,word in enumerate(words):
        if m==0:
            m+=1
            if word in (ascii_letters+"_"):
                continue
            else:
                print("第1个字符是非法字符")
        else:
            if word in (ascii_letters+digits+"_"):
                continue
            else:
                print("第%d个字符是非法字符" % (key+1))
#        i+=1
#if i==0:
#    print("%s是可用字符" % (words))

if __name__=="__main__":
    keycheck()
    wordcheck()