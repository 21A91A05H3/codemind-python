n=int(input())
a=list(map(int,input().split()))
es=0
os=0
for i in range(0,n):
    if i%2==0:
        es+=a[i]
    else:
        os+=a[i]
if abs(os-es)==0:
    print("YES")
else:
    print("NO")