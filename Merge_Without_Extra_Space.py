t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    ar=list(map(int,input().split()))
    br=list(map(int,input().split()))
    s=ar+br
    l=[]
    for i in s:
        if i not in l:
            l.append(i)
    l.sort()
    print(*l)
