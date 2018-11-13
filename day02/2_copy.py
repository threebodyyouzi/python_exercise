#!/usr/local/bin/python3.6
import sys
def copy_file():
    src=open(sys.argv[1],"rb")
    des=open(sys.argv[2],"wb")
    while True:
        data=src.read(4096)
        if not data:
            break
        des.write(data)
    src.close()
    des.close()

#copy_file()
print(__name__)