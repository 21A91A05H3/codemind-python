s=input()
d="0123456789"
l=[]
c=0
for i in s:
    if i in d:
        l.append(i)
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")