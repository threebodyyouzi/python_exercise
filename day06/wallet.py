#!/usr
import time
import pickle
import os
import json
money={"时间":time.strftime("%Y-%m-%d %H:%M:%S"),"余额":0,"开销":0,"收入":0,"备注":"default"}
def account_book(record,wallet):
	if os.path.exists(record):
#		with open(record,"r") as fobj:
#			if dict(fobj.readlines())["备注"]!="origin":
		print("\033[31;1m文件已存在，请创建新的账本文件\033[0m")
	else:
		with open(record,"w") as fobj:
			create=money.copy()
			create["备注"]="origin"
			create["余额"]=10000
			jsobj=json.dumps(create,ensure_ascii=False)
			fobj.write(jsobj+"\n")
		with open(wallet,"wb") as fobj:
			pickle.dump(10000,fobj)
			print("新的账本已经创建成功")
	pass
def add_money(record,wallet):
	if not os.path.exists(record):
		print("\033[31;1m账本文件不存在,请先创建账本\033[0m")
	else:
		try:
			change=int(input("收入："))
		except ValueError:
			print("\033[31;1m请输入正确的金额:\033[0m")
		else:
			note=input("备注: ")
			with open(wallet,"rb") as fobj:
				cash=pickle.load(fobj)+change
			add_account=money.copy()
			add_account.update({"收入":change,"备注":note,"余额":cash})
			with open(wallet,"wb") as fobj:
				pickle.dump(cash,fobj)
			with open(record,"a") as fobj:
				fobj.write(json.dumps(add_account,ensure_ascii=False)+"\n")
def use_money(record,wallet):
	if not os.path.exists(record):
		print("账本文件不存在,请先创建账本")
	else:
		try:
			change=int(input("支出："))
		except ValueError:
			print("请输入正确的金额")
		else:
			note=input("备注: ")
			with open(wallet,"rb") as fobj:
				cash=pickle.load(fobj)-change
			del_account=money.copy()
			del_account.update({"支出":change,"备注":note,"余额":cash})
			with open(wallet,"wb") as fobj:
				pickle.dump(cash,fobj)
			with open(record,"a") as fobj:
				fobj.write(json.dumps(del_account,ensure_ascii=False)+"\n")
def view_account(record,wallet):
	with open(record) as fobj:
		for line in fobj:
			print(line)
	with open(wallet,"rb") as fobj:
		cash=pickle.load(fobj)
		print("当前余额: %d" % cash)
	pass
def show_menu():
	account_path=input("账单路径:")
	project={"0":account_book,"1":add_money,"2":use_money,"3":view_account}
	prompt='''(0)创建账本
(1)新增收入
(2)新增开销
(3)查看金额
(4)退出
请输入你的选择：'''
		# if os.path.exists(record):
		# 	print("账本已存在")
		# else:
		# 	with open(record,"w") as fobj:
		# 		fobj.write()
	while True:
		choice=input(prompt).strip()[0]
		if choice not in "01234":
			print("错误输入，请重输")
			continue
		if choice=="4":
			break
		if not os.path.exists(account_path):
			os.makedirs(account_path)
		record=os.path.join(account_path,"record.txt")
		wallet=os.path.join(account_path,"wallet.wt")
		project[choice](record,wallet)


if __name__=="__main__":
	show_menu()


