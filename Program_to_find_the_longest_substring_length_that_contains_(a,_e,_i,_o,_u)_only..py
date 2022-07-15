n=input()
c=ma=0
vow="aeiouAEIOU"
for i in range(len(n)):
    c=0
    for j in range(i,len(n)):
        if n[j] in vow:
            c+=1
            if ma<c:
                ma=c
        else:
            break
print(ma)