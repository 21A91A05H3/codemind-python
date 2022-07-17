n=int(input())
arr=list(map(int,input().split()))
c=0
l=[]
for i in arr:
    if i not in l and i%2!=0:
        l.append(i)
        c+=1
print(c)
