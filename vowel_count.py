s=input()
n="aeiouAEIOU"
c=0
for i in range(len(s)):
    if s[i] in n:
        c+=1
print(c)