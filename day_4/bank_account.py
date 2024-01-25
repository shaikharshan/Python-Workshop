class bank_account:
    def __init__(self,balance):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('success depositing')
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance=self.balance+amount
            print("success")
        else:
            print("unsuccessful")
    def display(self):
        print(f"current balance is {self.balance}")
ob=bank_account()
ob.deposit(500)

