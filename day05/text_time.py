#!/usr/local/bin/python3.6
# import time
# print(time.time())
# print(time.localtime())
# print(time.asctime())
# print(time.ctime(0))
# print(time.localtime(0))
# print(time.strftime("%Y年%m月%d日 %H时%M分%S秒"))
# print(time.strftime("%a"))
# print(time.strftime("%A"))
# print(time.strftime("%h"))

from datetime import datetime,timedelta
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.ctime(datetime.now()))
t=datetime.now()
print(t-timedelta(days=150))
print(t+timedelta(days=100))
print(t-datetime(2018,6,29,9,0,0,0))
print(datetime(2019,1,1,0,0,0,0)-t)