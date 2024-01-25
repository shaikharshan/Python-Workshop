li=[6,5,4,3,2,1]
for i in range(1,len(li)):
    key=li[i]
    j=i-1
    while(j>=0 and key<li[j]):
        li[j+1]=li[j]
        j=j-1
    li[j+1]=key
    print(li)
