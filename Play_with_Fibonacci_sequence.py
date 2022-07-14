n=int(input())
a=0
b=1
c=0
while c<n:
    print(a,end=' ')
    x=a+b
    a=b
    b=x
    c+=1