import re

tmlt=open('C:/tmp/_template.txt','r', encoding="utf8")
rows = tmlt.readlines()
searchp=re.compile(r'<.*todo.*>')
counter=0

for row in rows:
    match=searchp.match(row)
    if match:
        print(match)
        counter+=1
print(counter)