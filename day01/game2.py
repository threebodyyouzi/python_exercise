#!/usr/local/bin/python3.6
import random
win_mode=(["石头","剪刀"],["剪刀","布"],["布","石头"])
choice = {1: "石头", 2: "剪刀", 3: "布"}
while 1 :
    _computer_choice=random.randint(1,3)
    _computer=choice[_computer_choice]

    _player_choice=input('''请输入您的选择: 
(1)石头
(2)剪刀
(3)布
''')
    if _player_choice not in ("1","2","3"):
        print("错误输入,请输入1,2,3")
        continue
    else :
        _player = choice[int(_player_choice)]



    if _computer == _player :
        result=print("平局")
    elif [_player,_computer] in win_mode :
        result =print("你赢了")
    else :
        result =print("你输了")