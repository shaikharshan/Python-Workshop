def add(*args): #**kwargs for dictionary
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(1,2,3,4)
#returning an object
#variables have different scope because of stacking
#myprint(lname="sh",fname="ar")
#add(maths="1",science="2")
#segmentation,runtime error