s=input()
a=input()
c=0
for i in range(len(s)):
    if s[i]==a:
        print(True)
        print(i)
        c=1
        break
if c==0:
    print(False)