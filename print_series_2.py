for i in range(1,13):
    print("\n")
    if i<6:
        for j in range(5,5-i,-1):
            print(j,end="")
    else:
        for k in range(5,i-5,-1):
            print(k,end="")