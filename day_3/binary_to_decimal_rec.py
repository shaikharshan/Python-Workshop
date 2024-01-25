def btd(num):
    
    if num==0:
        return 0
    elif num==1:
        return 1 
    else:
        rem=num%10
        return ((rem))+2*btd(num//10)
print(btd(1010))
