class complex_number:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def print(self):
        print(f"({self.real})+({self.img})i")
    def add(self,obj):
        new=complex_number(0,0)
        new.real=self.real+obj.real
        new.img=self.img+obj.img
        return new
obj1=complex_number(2,-4)
obj2=complex_number(1,3)
# obj3=obj1+obj2


    