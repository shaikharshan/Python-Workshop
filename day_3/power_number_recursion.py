def power(a,b):
    mul=a
    if b==0:
        return 1
    else:
        return mul*power(a,b-1)
print(power(2,3))
