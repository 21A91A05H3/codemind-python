n=int(input())
arr=list(map(int,input().split()))
avg=0
sum=0
for i in range(0,n):
    sum=sum+arr[i]
    avg=sum/n
print("%.2f"%avg)