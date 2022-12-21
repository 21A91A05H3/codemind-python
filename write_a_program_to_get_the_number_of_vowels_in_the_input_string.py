s=input().lower()
a="aeiou"
c=0
for i in s:
    if i in a:
        c+=1
if c==0:
    print("0")
else:
    print(c)