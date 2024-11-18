class book:

    def __init__(self , n , a , p):
        self.title = n
        self.author = a
        self.price = p
    
    def view(self):
        print(f"\n\n*******************************")
        print(f"title = {self.title}")
        print(f"author = {self.author}")
        print(f"price = {self.price}")


n = input("TITLE : ")
a = input("AUTHOR NAME : ")
p = int(input("PRICE : "))

t1 = book(n,a,p)
t1.view()