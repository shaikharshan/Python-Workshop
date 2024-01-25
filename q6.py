#prime no.
flag = 0
num = int(input("enter the no. "))
if num<2:
    print("not a prime no.")
elif num == 2:
    print("prime no.")
else:
    for i in range(2,num):
        if num % i == 0:
            flag=1
            break
    if flag == 0:
        print("it is a prime")
    else:
        print("not prime")