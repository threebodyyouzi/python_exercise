origin_line=[]
entry=""
numbers=0
while entry!="ok":
	entry=input('请输入数字到队列中(输入ok完成队列):')
	if entry.isdigit():
		origin_line.append(entry)
		numbers+=1
	else:
		print("请输入数字")
		continue

for number in range(0,numbers):
	tmp=origin_line[number]
	for other_number in range(number,numbers):
		if tmp<origin_line[other_number]:
			origin_line[number] = origin_line[other_number]
			origin_line[other_number] = tmp
			tmp = origin_line[number]



print(origin_line)

