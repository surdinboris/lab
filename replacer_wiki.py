import re
import os

debug=False
workdir='c:/tmp/wikireplace/wiki_n1/'
fileist=os.listdir(workdir)
searchop=re.compile(r".*further\s*notice.*")
match=lambda x,y: x.match(y) if x.match(y) else None
counter=0

def analyze(filename):
    global counter
    file=open(os.path.join(workdir, filename), 'r', encoding="utf-8")
    print("opening file "+file.name)
    rows=file.readlines()
    matched=0
    for row in rows:
        rowid=rows.index(row)
        if match(searchop, row):
            matched=1
            newrow= row.replace('further','').replace('notice','FN')
            rows[rowid]=newrow
            counter+=1
            print(newrow)
    if matched:
        print(type(rows))
        file=open(os.path.join(workdir, filename), 'w', encoding="utf-8")
        file.writelines(rows)
    file.close()

for f in fileist:
    analyze(f)

print('found',counter)

