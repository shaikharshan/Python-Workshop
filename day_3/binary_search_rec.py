def binary(li,key,mid):
    low=0
    high=len(li)-1
    mid=low+high
    if key==li[0]:
        return li[0]
    elif key==li[len(li)-1]:
        return li[len(li)-1]
    else:
    