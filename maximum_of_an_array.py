n=int(input())
arr=list(map(int,input().split()))
max=arr[0]
for i in range(0,n):
    if arr[i]>max:
        max=arr[i]
print(max)        