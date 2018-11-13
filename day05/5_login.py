#!/usr/local/bin/python3.6
import getpass
users={}
def sign_in():
    user_name=input("请输入你的账号名:")
    user_pass=getpass.getpass()
    if user_name not in users:
        print("不存在该用户")
    if users[user_name] == user_pass:
        print("登入成功")
    else:
        print("登入失败")

def sign_up():
    user_name = input("请输入你的账号名:")
    if user_name in users:
        print("该用户已存在")
    else:
        user_pass = input("请输入你的密码:")
        users.update({user_name:user_pass})
        print("用户%s创建成功" % user_name)

def show_menu():
    cmds={"0":sign_in,"1":sign_up}
    prompt='''(0)登入
(1)注册
(2)quit
请输入你的选择:'''
    while True:
        choice = input(prompt).strip()
        if choice not in "012":
            print("错误输入,请重输")
            continue
        elif choice == "2":
            break
        cmds[choice]()

if __name__ == "__main__":
    show_menu()
