class book:
    def __init__(self,title,author,price):  #here self is ob
        self.title=title
        self.author=author
        self.price=price
    def get_title(self):
        return self.title
ob=book("T","A",150) 
print(get_title())

#getter setter