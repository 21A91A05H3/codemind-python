n,m=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
l=[]
for i in arr:
    if i in brr:
        if i not in l:
            l.append(i)
print(*l)            