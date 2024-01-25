def print_rec(n):
    if n==0:
        return 0
    else:
         print_rec(n-1)
         print(n)
print_rec(8)