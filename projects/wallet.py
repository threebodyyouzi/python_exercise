import time
import pickle
import os
import json
money={"时间":time.strftime("%Y-%m-%d %H:%M:%S"),"余额":0,"开销":0,"收入":0,"备注":"default"}
def account_book(record,wallet):
	if os.path.exists(record):
		with open(record,"r") as fobj:
			if dict(fobj.readlines())["备注"]!="origin":
			# if pickle.load(fobj)["备注"] != "origin":
				print("文件已存在，请创建新的账本文件")
	with open(record,"w") as fobj:
		create=money.copy()
		create["备注"]="origin"
		create["余额"]="10000"
		jsobj=json.dumps(create,ensure_ascii=False)
		fobj.write(jsobj+"\n")
	with open(wallet,"wb") as fobj:
		pickle.dump(10000,fobj)
		print("新的账本已经创建成功")
	pass
def add_money(record,wallet):
	change=int(input("收入："))
	note=input("备注: ")
	with open(wallet,"rb") as fobj:
		cash=pickle.load(fobj)+change
	add_account=money.copy()
	add_account.update({"收入":change,"information":note,"余额":cash})
	with open(wallet,"wb") as fobj:
		pickle.dump(cash,fobj)
	with open(record,"a") as fobj:
		fobj.write(json.dumps(add_account,ensure_ascii=False)+"\n")
	pass
def use_money(record,wallet):
	change=int(input("支出："))
	note=input("备注: ")
	with open(wallet,"rb") as fobj:
		cash=pickle.load(fobj)-change
	del_account=money.copy()
	del_account.update({"支出":change,"information":note,"余额":cash})
	with open(wallet,"wb") as fobj:
		pickle.dump(cash,fobj)
	with open(record,"a") as fobj:
		fobj.write(json.dumps(del_account,ensure_ascii=False)+"\n")
	pass
def view_account(record,wallet):
	with open(record) as fobj:
		for line in fobj:
			print(line)
	with open(wallet,"rb") as fobj:
		cash=pickle.load(fobj)
		print("当前余额: %d" % cash)
	pass
def show_menu(record,wallet):
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
		choice=input(prompt).strip()
		if choice not in "01234":
			print("错误输入，请重输")
			continue
		project[choice](record,wallet)

if __name__=="__main__":
	show_menu("D://record.txt","D://wallet.txt")


