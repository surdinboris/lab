import os
class generate:
    def __init__(self):
        self.prefs = ['052', '054', '051', '058']
        self.body = range(0, 9)
        self.otpname = 'phones.log'
        self.otpdir = os.path.abspath(os.curdir)
        self.phonegen(self.prefs, self.body,self.otpdir,self.otpname)

    def phonegen(self,prefs,body,otpdir,otpname):
        fh = open(os.path.join(otpdir, otpname), 'w')
        print("Building phonelist in: %s..." % fh.name)
        for i in prefs:
            for r in body:
                res=(lambda x,y: ''.join((x,str(y).zfill(7))))
                fh.writelines(res(i,r)+'\n')
        fh.close()
        print('Done.')


rt=generate()


