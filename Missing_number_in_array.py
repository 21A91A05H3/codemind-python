n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    for i in range(1,a+1):
        if i not in b:
            print(i)