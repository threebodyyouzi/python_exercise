#!/usr/local/bin/python3.6
import shutil
#shutil.copyfileobj(open("/etc/passwd","rb"),open("/tmp/mima.txt","wb"))
#shutil.copyfile("/etc/passwd","/tmp/mima.txt")
#shutil.copy("/etc/passwd","/tmp/passwd2")
#shutil.copy2("/etc/passwd","/tmp/")
#shutil.move("/tmp/passwd","/tmp/mima2")
#shutil.copy("/root/a.txt","/tmp/a1.txt")
#shutil.copy2("/root/a.txt","/tmp/a2.txt")
#shutil.copytree("/tmp/","/root/")
#shutil.copytree("/tmp","/tmp2")
#shutil.rmtree("/tmp2")
# shutil.copy2("/root/a.txt","/tmp/a1.txt")
# shutil.copymode("/root/a.txt","/tmp/a1.txt")
#shutil.copystat("/etc/passwd","/tmp/a1.txt")
#shutil.copystat("/etc/fstab","/tmp/a1.txt")
#shutil.chown("/tmp/a1.txt",user="Student",group="Student")
# with open("/tmp/passwd","r") as src_file:
#     with open("/tmp/a3.txt","w") as des_file:
#         shutil.copyfileobj(src_file,des_file)
# open("/etc/passwd","rb").close()
# open("/tmp/a3.txt","wb").close()
# with open("/etc/passwd","rb") as src_file:
#      with open("/tmp/a3.txt","wb") as des_file:
#          shutil.copyfileobj(src_file,des_file)
#          print(des_file.closed)
#          des_file.seek(0,0)
# print(des_file.closed)
#with open("/tmp/a3.txt","rb") as des_file:
#    print(des_file.read())

####################################################
# (a,b,c)=(1,2,3)
# print(a)
# print(b)
# print(a,b)

import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("print"))
# print(keyword.iskeyword("import"))

word=input("待查字符:")
if word in keyword.kwlist:
    print(word+"是关键字")
else:
    print(word+"不是关键字")