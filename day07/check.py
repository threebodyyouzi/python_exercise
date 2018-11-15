#!/usr/local/bin/python3.6
import hashlib
import sys
# def md5(data):
#     m=hashlib.md5()
#     m.update(data.encode("utf8"))
#     print(m.hexdigest())
# if __name__ == '__main__':
#     with open("/etc/passwd") as fobj:
#         while True:
#             data=fobj.read(4096)
#             if not data:
#                 break
#             md5(data)
    # print(lock("hello"))
def md5(fname):
    m=hashlib.md5()
    with open(fname,"rb") as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
if __name__ == '__main__':
    print(md5(sys.argv[1]))