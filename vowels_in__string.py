s=input()
n="a,e,i,o,u,A,E,I,O,U"
l=[]
for i in s:
    if i in n and i not in l:
        l.append(i)
print(*l)