#mutability checking
def wrapper(obj):
    print('wrapper init')
    obj['par1key']='newvalfromWrapper'
obj={'par1key':'par1val'}

#print(obj)
#wrapper(obj)
#print(obj)


#passing a function checking
def wrapperF(func):
    func('wrapper init')

def func(t):
    print('func init', t)

wrapperF(func)

func('external')

#wrapper(obj)

