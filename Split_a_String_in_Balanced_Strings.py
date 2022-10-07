s=input()
r=0
l=0
rl=0
for i in s:
    if i=="R":
        r+=1
    elif i=="L":
        l+=1
    if l==r:
        rl+=1
print(rl)