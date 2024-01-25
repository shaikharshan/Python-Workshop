num = int(input("enter no. "))
cnum = num
while cnum>0:
    rem = cnum % 10
    cnum = cnum//10
    print(rem,end="")
