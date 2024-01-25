for i in range(1,31):
    for j in range(1,31):
       for k in range(1,31):
        if k**2 == i**2 + j**2:
             print(i,j,k)