li=[34,21,1,4,23,87]
l2=[0,0]

for i in range(0,len(li)):
    for j in range(0,len(li)):
        if li[i]<li[j]:
            dif = l2[1]-l2[0]
            if dif>(li[j]-li[i]):
                ans = dif
            l2[0]=li[i]
            l2[1]=li[j]
            print(l2)
print(ans)
