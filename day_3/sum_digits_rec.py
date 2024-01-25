def sum_dig(num):
    if num==0:
        return 0
    else:
        rem = num%10
        return rem+sum_dig(num//10)
print(sum_dig(12345))