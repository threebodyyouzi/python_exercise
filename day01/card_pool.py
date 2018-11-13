#!/usr/local/bin/python3.6
import random
result=[]

i=0

while result.count("SSR")<1:
#for j in range(1,11):
    time = 0
    while time<10:
        player_get=int(random.randint(1,100))
        if player_get==1:
            #print("你获得一张SSR")
            result.append("SSR")
        elif player_get>1 and player_get<=40:
            #print("你获得一张SR")
            result.append("SR")
        else:
            #print("你获得一张R")
            result.append("R")
        time+=1
    i+=1
    if result.count("SSR")==1:
        break


print('SSR的数量为'+str(result.count("SSR")))
print('SR的数量为'+str(result.count("SR")))
print('R的数量为'+str(result.count("R")))
print(i)