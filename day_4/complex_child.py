class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
class real(complex):
   def __init__(self, real):
       super().__init__(real,0)
