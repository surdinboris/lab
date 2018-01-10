import os
class generate:

    def __init__(self):
        self.prefs = ['052', '054', '051', '058']
        self.body = range(0, 9)
        self.otpname = 'phones.log'
        self.otpdir = os.path.abspath(os.curdir)

    def phonegen(self):
        fh = open(os.path.join(self.otpdir, self.otpname), 'w')
        print("Building phonelist in: %s..." % fh.name)
        for i in self.prefs:
            for r in self.body:
                res=(lambda x,y: ''.join((x,str(y).zfill(7))))
                fh.writelines(res(i,r)+'\n')
        fh.close()

        print('Done.')

rt1=generate()
rt1.prefs=['045','094']
rt1.phonegen()
