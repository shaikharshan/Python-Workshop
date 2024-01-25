for i in range(1,51):
    if i%3==0:
        print("ACM")
    elif i%5 == 0:
        print("VNIT")
    elif(i%3 == 0 and i%5==0):
        print("ACM VNIT",end = "divisibleby15")