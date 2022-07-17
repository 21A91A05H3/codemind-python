n=int(input())
arr=list(map(int,input().split()))
t=int(input())
l=[]
for i in range(len(arr)):
    if arr.count(arr[i])==t:
        if arr[i] not in l:
            l.append(arr[i])
if len(l)>0:
    print(*l)
else:
    print(-1)