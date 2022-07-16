def iso():
    return len(s)==len(set(s.lower()))
s=input()
if iso()==True:
    print("True")
else:
    print("False")