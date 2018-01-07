class lam:
    def __init__(self):
        print('class laminit')

    def imports(self, *args, **kwargs):
        print(args,kwargs)
gh=lam()

gh.imports('dfg','dfgdfg')
