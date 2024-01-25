def gcd_rec(a,b):#b>a
    rem=a%b
    if rem==0:
        return b
    else:
        return gcd_rec(a,rem)
print(gcd_rec(24,18))