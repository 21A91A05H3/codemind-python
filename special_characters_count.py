
s=input()
n='abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM '
c=0
for i in s:
    if i not in n:
        c+=1
print(c)