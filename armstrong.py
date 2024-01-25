#sum of cubes = number itself ex. 371

for i in range(10,501):
    sum = 0
    num = i
    while num>0:
        rem = num%10
        sum = sum + rem**3
        num = num//10
    if sum == i:
        print(i)