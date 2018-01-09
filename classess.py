class lam:
    def __init__(self, *args, **kwargs):
        self.t=args
        print(self.t)

    def imports(self, *args, **kwargs):

        self.eec=kwargs['u']
        print(self.eec)
        return(args,kwargs)

gh=lam
gh().__init__('sfsdsfasddasdasda')
gh().imports('dfg',u="data")
print(id(gh))
ty=(gh().imports('dfg',u="newdta"))
print(id(ty))
#print('retrieving',gh.u)