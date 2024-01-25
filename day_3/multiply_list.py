def multi(l1):
    mul=l1[0]
    for i in range(1,len(l1)):
        mul=mul*i
    return mul
li=[5,1,2,-3,-4]
print(multi(li))