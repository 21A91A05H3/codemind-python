s1=list(input().lower().replace(' ',''))
s2=list(input().lower().replace(' ',''))
l=[]
for i in s1:
    if i not in s2 and i not in l:
        l.append(i)
for i in s2:
    if i not in s1 and i not in l:
        l.append(i)
print(len(l))