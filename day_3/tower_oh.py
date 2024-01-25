def toh (n,s,d,a):#number,source,destination,auxillary
    if n>0:
        toh(n-1,s,a,d)
        print(f"{s} to {a}")
        toh(n-1,a,d,s)
toh(3,"a","b","c")