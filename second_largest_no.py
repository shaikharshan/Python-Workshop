li=[11,2,14,58,32]
# 2,11,14,32,58
for i in range(0,6):
    for j in range(i+1,5):
        if li[j]<li[i]:
            temp = li[j]
            li[j] = li[i]
            li[i] = temp
print(li)
print(li[3]) #second largest
print(li[1])#second smallest
