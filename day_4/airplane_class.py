class airplane:
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def check(self,speed):
        if speed>=self.min and speed<=self.max:
            print("yes")
        else:
            print("No")
ob=airplane(40,50)
ob.check(35)