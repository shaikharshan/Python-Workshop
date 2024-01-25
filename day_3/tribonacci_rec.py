def tribo(n):
    if n<2:
        return 0
    elif n==3:
        return 1
    else:
        return tribo(n-1)+tribo(n-2)+tribo(n-3)
# print(tribo(4))
for i in range(0,10):
    print(tribo(i))       