n=int(input())
while(1):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    if sum>0 and sum<9:
        print(sum)
        break
    else:
        n=sum