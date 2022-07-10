n=int(input())
arr=list(map(int,input().split()))
se=int(input())
for i in range(0,n):
    if arr[i]==se:
        print("True")
        break
else:
    print("False")