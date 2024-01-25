li=[2,2,1,0,2,2]
cnt1=cnt2=cnt3=0
#l2=li
for i in range(0,len(li)):
    if li[i]==0:
        cnt1=cnt1+1
    elif li[i]==1:
        cnt2=cnt2+1
    elif li[i]==2:
        cnt3=cnt3+1
for j in range(0,len(li)):
    if j<cnt1:
        li[j]=0
    elif j>cnt1 and j<cnt1+cnt2:
        li[j]=1
    elif j>cnt2+cnt1 and j<cnt1+cnt2+cnt3:
        li[j]=2
print(li)



