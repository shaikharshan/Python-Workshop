class base:
    __i=2 #private
    j= "str"#public
    #for protected _k
    def myprint(self): #methods 
        print("in base")

class derived(base):
    def myprint(self):
        print("in derived")
b=base()
b.myprint
d=derived()
d.myprint()
#obj1__add__obj2
def __add__(self,obj):
    newobj = complex(0,0)
    newobj.real = self.real + obj.real
    newobj.img = self.img + obj.img
    return newobj
obj1=complex(4,2)
obj2=complex(4,2)
obj3=obj1+obj2
obj3.printcomplex()

#polymorphisim not present in python to take multiple parameters ocnsider null parameters
# virtual functions
#  b1 = new base()
#  b2 = new derived()