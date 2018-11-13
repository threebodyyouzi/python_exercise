#!/usr/local/bin/python3.6
from time import sleep
def cartoon():
    while True:
        print("#"*20,end="")
        for num in range(0,20):
            print("\r%s@%s" % ("#"*num,"#"*(19-num)),end="")
            sleep(0.3)
#    while True:
#       print("\r%s@%s" % ("#" * num, "#" * (19 - num)))
if __name__=="__main__":
    cartoon()
