n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
s=0
c=0
for i in l:
    if i%2==0:
        a.append(i)
        s+=1
    if i%2!=0:
        b.append(i)
        c+=1
print(s,c,end='')