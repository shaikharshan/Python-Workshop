for i in range(5,9):
    print(i)
#starting value is 0
#condition i <=9
j=4
while j<10:
    print(j)
    j=j+1


#lists
l1 = [1,2,3,4]
print(l1)
print(len(l1))
for i in range(len(l1)):
    print(l1[i])


l2=[23,33,1,3,4]
print(l2[2:5])
l2.append(300)
print(l2)


#tuples
# immutable
t1=(3,5)
print(t1)

#dicitionaries custom index
fruits = {
    "apples" : 100,
    "banana" : 34,
    "grapes" : 25
}
print(fruits["apples"])
print(fruits.keys())
print(fruits.values())
for i in fruits.keys():
    print(i,fruits[i])


#set
#duplicates are not allowed
a={2,3,4}