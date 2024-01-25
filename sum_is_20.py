# a+b+c+d=20
for i in range(1,21):
    for j in range(i,21):
        for k in range(j,21):
            for l in range(k,21):
                if i+j+k+l==20:
                    print(i,j,k,l)
