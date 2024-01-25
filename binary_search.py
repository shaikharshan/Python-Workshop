li=[5,6,7,8,9]#sorted
key=int(input("enter key "))
low=li[0]
high=len(li)-1
ans=-1
while(low<=high):
    mid = (low+high)//2
    if(key==li[mid]):
        ans=mid
        break
    elif(key>li[mid]):
        low=mid+1
    else:
        high=mid-1
    print(ans)

