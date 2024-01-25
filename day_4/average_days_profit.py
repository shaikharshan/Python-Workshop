class average:
    def __init__(self,days,profit):
        self.days=days
        self.profit=profit
    def avg(self):
        sum=0
        for i in range(0,len(self.profit)):
            sum=sum + (self.profit[i]/self.days)
        return sum
ob=average(4,[1,2,3,4])
print(ob.avg())
