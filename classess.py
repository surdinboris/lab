class lam:
    y=0
    def __init__(self, *args, **kwargs):
        self.t=args
        print(self.t)

    def imports(self, *args, **kwargs):

        self.eec=kwargs['u']
        print(self.eec)
        return(args,kwargs)

gh=lam('uu')

print(type(gh))
gh.t=6

print(gh.t)