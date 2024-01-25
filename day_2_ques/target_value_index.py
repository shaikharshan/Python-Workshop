li=[12,15,18,20,25]
key = int(input("enter key "))
low=0
high=len(li)

while low<=high:
    mid =(low+high)//2
    if key==li[mid]:
        ans=mid
        print(ans)
        break
    elif key<li[mid]:
        high=mid-1
    elif key>li[mid]:
        low=mid+1
    else :
        print("key has to be placed at ",low,"index")