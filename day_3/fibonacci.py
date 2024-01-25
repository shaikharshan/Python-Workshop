#1,1,2,3,5,8,13....using rec
def fibo_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)
fibo_rec(4)