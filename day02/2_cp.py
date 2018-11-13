#!/usr/local/bin/python3.6
src_obj=open("/bin/ls","rb")
des_obj=open("/root/ls","wb")

while 1:
    data=src_obj.read(4096)
    if not data:
        break
    des_obj.write(data)
src_obj.close()
des_obj.close()
