def large(li):
    for i in range(0,len(li)):
        for j in range(i,len(li)):
            if li[j]<li[i]:
                temp=li[j]
                li[j]=li[i]
                li[i]=temp
    print(li)
    print(li[-1])
l=[1,4,2,5,76,99,23]
large(l)