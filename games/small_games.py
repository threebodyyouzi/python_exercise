#利用python编写的小游戏集合
from random import randint,choice
from string import digits
def info():
	print('''拥有的游戏有：
(a)石头剪刀布
(b)猜数字''')

def a():
	equal_time=0
	win_time=0
	lose_time=0
	while True:
		all_choice={1:"石头", 2:"剪刀", 3:"布"}
		win_mode=(["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"])
		computer_choice=randint(1,3)
		computer_result=all_choice[computer_choice]   #给电脑赋予一个随机的结果

		player_choice=input('''请出拳：
(1)石头
(2)剪刀
(3)布
''')
		if player_choice not in ("1", "2", "3"):
			print("错误输入，请输入1/2/3")
			continue
		else:
			player_choice=int(player_choice)
			player_result=all_choice[player_choice]

		if player_result==computer_result:
			print("平局")
			equal_time+=1
		elif [player_result, computer_result] in win_mode:
			print("这局你赢了")
			win_time+=1
		else:
			print("这局你输了")
			lose_time+=1

		if win_time==2:
			result=print("winner")
			break
		elif lose_time==2:
			result=print("lose")
			break
		else:
			continue
	return result

def b():
	time=1
	computer_number=randint(1,100)
	while True:
		player_number=input('请输入你猜的数字:')
		if player_number.isdigit():
			player_number = int(player_number)
			if player_number<1 or player_number>100:
				print("超出范围，数字范围1—100")
			else:
				if player_number < computer_number:
					print("猜小了")
				elif player_number > computer_number:
					print("猜大了")
				else:
					result = print("猜对了,总共猜了" + str(time) + "次")
					break
				time += 1
		else:
			print("请输入数字")
			continue

		if time==6:
			result=print("竞猜失败，答案是"+str(computer_number))
			break
	return result



if __name__=="__main__":
	#a()
    b()


