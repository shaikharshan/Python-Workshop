class kmath:
    def __init__(self,k):
        self.k=k
    def add(self,n):
        return self.k+n
    def sub(self,n):
        return self.k-n
    def multi(self,n):
        return self.k*n
    def div(self,n):
        if n!=0:
            return self.k/n
ob=kmath(5)
print(ob.add(4))
print(ob.sub(4))
print(ob.multi(4))
