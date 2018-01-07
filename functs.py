import os
prefs=['052','054','051','058']
body=range(0, 9999999)
otpname='phones.log'
otpdir=os.path.abspath(os.curdir)
fh=open(os.path.join(otpdir,otpname),'w')
def phonegen(prefs,body):
    for i in prefs:
        for r in body:
            res=(lambda x,y: ''.join((x,str(y).zfill(7))))
            fh.writelines(res(i,r)+'\n')
    fh.close()
print("Building phonelist in: %s..." %fh.name)

phonegen(prefs,body)

print('Done.')

