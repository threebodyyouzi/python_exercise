import re
a="bit bat but bet"
bt="bat|bit|bet"
m=re.search(bt,"bet")
print(m.group())
