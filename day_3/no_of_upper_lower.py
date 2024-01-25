def uplow(str):
    cnt1=cnt2=0
    for i in range(0,len(str)):
        if str[i]>=chr(97) and str[i]<=chr(122): #upper
            cnt1=cnt1+1
        elif str[i]>=chr(65) and str[i]<=chr(90):  #lower
            cnt2=cnt2+1
    return cnt1,cnt2
print(uplow("AAAArr"))