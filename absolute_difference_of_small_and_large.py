n=list(map(str,input().split()))
a=0
b=0
for i in n:
    s=ord(min(i))
    a+=s
    l=ord(max(i))
    b+=l
    print(abs(a-b),end=' ')
    a=b=0