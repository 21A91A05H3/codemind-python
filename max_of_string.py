s=input()
l=[]
for i in range(len(s)):
    l.append(ord(s[i]))
print(chr(max(l)))