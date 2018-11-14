#!/usr/local/bin/python3.6
import random
def exam():
# a=random.randint(1,100)
# b=random.randint(1,100)
    nums=[random.randint(1,100) for i in range(2)]
    ops=["+","-","/"]
    op=random.choice(ops)
    t=0
    nums.sort(reverse=True)
    equal=str(nums[0]) + op + str(nums[1])
    answer=("%.2f" % eval(equal))
    while t<3:
        try:
            player=input(equal+"的值是多少?")
            if ("%.2f" % float(player))==answer:
                print("答对了")
                break
            elif t<2:
                print("答错了,再答一次")
            t+=1
        except ValueError:
            continue
    if t==3:
        print("正确答案是"+str(answer))
def main():
    prompt='''continue?(Y/N)'''
    while True:
        exam()
        try:
            choice=input(prompt).rstrip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print("\nBye-bye")
            choice="n"
        if choice == "Y" or choice=="y":
            continue
        else:
            break
    pass
if __name__ == '__main__':
    main()

