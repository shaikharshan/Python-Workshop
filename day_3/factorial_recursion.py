def fact(n):
    if n==1:
        return n
    else:

        return n*fact(n-1)

f=fact(5)
print(f)