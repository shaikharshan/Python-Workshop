class food:
    def __init__(self,veg,price,availability):
        self.veg=veg
        self.price=price
        self.availability=availability
    def condition(self):
        if self.veg=="veg" and self.price>=1000 and self.availability=="available":
            print("True")
        else:
            print("False")

c1=food("veg",125,"available")
c1.condition()