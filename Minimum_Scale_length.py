n=int(input())
arr=list(map(int,input().split()))
hcf=arr[0]
i=1
while(i<n):
    if(arr[i]%hcf==0):
        i+=1
    else:
        hcf=arr[i]%hcf
print(hcf)