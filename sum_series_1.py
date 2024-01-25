# 1+2/(1+2)+3/(1+3)+4/(1+4)
num = int(input("enter n "))
sum1 = sum2 = 0
for i in range(1,num+1):
    j=1
    sum1=0
    while j<=i:
        sum1 = sum1 + j
        j=j+1
    sum2 = sum2 + i/sum1
print(sum2)