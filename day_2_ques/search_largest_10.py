li=[10,21,900,59,100]
for i in range(0,len(li)):
    for j in range(i,len(li)):
        if li[j]<li[i]:
            temp=li[j]
            li[j]=li[i]
            li[i]=temp
for k in range(0,len(li)):
    if li[k]%10==0:
        ans=li[k]
print(ans)