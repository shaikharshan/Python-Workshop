class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def print(self,real,img):
        print(f"{self.real}+{self.img}j")
ob=complex(2,3)
ob.print(2,4)