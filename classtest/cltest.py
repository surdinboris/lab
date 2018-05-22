class Tst():
    def printcname(self):
        print('Tst class')


nobjTst= Tst()

def newprintcname(self):
    print('new Tst class')


Tst.printcname1 = newprintcname

nobjTst.printcname()

nobjTst.printcname1()
