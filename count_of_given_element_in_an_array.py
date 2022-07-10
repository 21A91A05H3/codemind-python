n=int(input())
arr=list(map(int,input().split()))
se=int(input())
c=0
for i in range(0,n):
    if arr[i]==se:
        c+=1
print(c)        