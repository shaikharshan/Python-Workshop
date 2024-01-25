class complex:
    # real=1  can have values

    #obtain private variables using getters setters
    # img=2

    def __init__(self,x,y):  #for taking variable values
        self.real=x
        self.img=y
    def printcomplex(self):
        print(self.real,"+",self.img,"j")
    def __add__(self,obj):
        newobj = complex(0,0)
        newobj.real = self.real + obj.real
        newobj.img = self.img + obj.img
        return newobj
obj1=complex(4,2)
obj2=complex(3,2)
obj3=obj1+obj2
obj3.printcomplex()