def sum(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
t=sum(25,2)
print('the result are')
for i in t:
    print(i,end=',')
