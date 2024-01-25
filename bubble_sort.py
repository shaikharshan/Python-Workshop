li=[5,3,4,2,8,1]
for i in range(0,len(li)):
    for j in range(0,len(li)-i):
        if li[j]>li[i]:
            temp = li[j]
            li[j]=li[i]
            li[i]=temp
print(li)   