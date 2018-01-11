import re
import os

tmplt=open(os.path.join(os.getcwd(),'_template.txt'),'r', encoding="utf8")
outptmplt=open(os.path.join(os.getcwd(),'_otemplate.txt'),'w', encoding="utf8")
rows = tmplt.readlines()
searchop=re.compile(r".*<todo.*>")
searchcl=re.compile(r".*</todo.*>")
counter=0
rowcollect=False
for row in rows:
    match=lambda x,y: x.match(y) if x.match(y) else None
    counter+=1
    oneliner=[]
    if match(searchop,row):
        print(match(searchop,row), 'open tag row %d' %counter )
        oneliner.append(counter)
    if match(searchcl, row):
        print(match(searchcl, row), 'closed row %d' %counter )
        oneliner.append(counter)
        if len(oneliner)== 2 and oneliner[0] == oneliner[1]:
            print('tag opened and closed in the same row')
    else:
        print(row, 'just row %d' %counter )
        rowcollect=True

