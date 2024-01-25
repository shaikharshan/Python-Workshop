li=[2,2,4,1,3]
for i in range(1,len(li)-1):
    sum1=sum2=0
    for j in range(0,len(li)):
        if j<i:
            sum1 = sum1+li[j]
        elif j>i:
            sum2 = sum2+li[j]
       # print(sum1,sum2,li[i])
        if li[i]==sum1+sum2:
            print(li[i])
        #prefix sum
        #sliding window approach