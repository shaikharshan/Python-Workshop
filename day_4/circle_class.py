class circle:
    def __init__(self,radius):
        self.radius=radius
    def comp_area(self):
        return 3.14*self.radius**2
    def peri(self):
        return 2*3.14*self.radius
ob=circle(4)  #methods are invoked on object
print(ob.comp_area())
print(ob.peri())