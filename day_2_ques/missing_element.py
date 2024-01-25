li=[1,2,3,5]
sum1=sum2=0
for i in range(0,len(li)):
    sum1 =sum1+li[i]
for j in range(1,len(li)+2):
    sum2=sum2+j
print(sum2-sum1)