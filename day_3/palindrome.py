def pd(str):
    status=0
    for i in range(0,len(str)):
        if str[i]==str[len(str)-i-1]:
            status=1
    if status==1:
        print("palindrome")
    else:
        print("not palindrome")
pd("MALAYALAM")
pd("arshan")
