li=[1,5,2,3]
for i in range(0,len(li)):
    for j in range(0,len(li)):
        if (li[j]%li[i]==0 and li[j]!=li[i]):
            print(li[i],li[j])
