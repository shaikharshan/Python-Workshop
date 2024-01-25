#for [0,0,0,0,0,0] => ans = n such that n-n shows 0
li = [0,0,0,1,1,1]
cnt=0
ans=len(li)
low=li[0]
high=len(li)-1
while low<=high:
    mid=(low+high)//2
    if li[mid] == 0:
        low=mid+1
    elif li[mid] == 1:
        high=mid-1    
        ans=mid
print(len(li)-ans)