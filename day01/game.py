#!/usr/local/bin/python3.6
import random
choice={1:"石头",2:"剪刀",3:"布"}
_computer_choice=random.randint(1,3)
_computer=choice[_computer_choice]

_player_choice=int(input('''请输入您的选择:
(1)石头
(2)剪刀
(3)布
'''))
if _player_choice in (1,2,3):
    _player=choice[_player_choice]
else :
    print("错误输入,输入范围1-3")
    exit(0)

win_mode=(["石头","剪刀"],["剪刀","布"],["布","石头"])

if _computer == _player :
    print("平局")
elif [_player,_computer] in win_mode :
    print("你赢了")
else :
    print("你输了")