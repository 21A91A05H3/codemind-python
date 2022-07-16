s=input()
s=s.lower()
str=""
for i in s:
    str=i+str
if s==str:
    print("True")
else:
    print("False")