def sum(a,**args):
    s=0
    s=s+a
    for i in args:
        s+=args[i]
    print(s)


sum(1,b=2,c=3,d=4,e=5)