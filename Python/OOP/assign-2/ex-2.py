#ex-2.
class Product:
    def __init__(self,p_no,p_name,price):
        self.p = p_name
        self.pr = price
        self.n = p_no
        
    def Display(self):
        print(f"{self.n}. Product Name ={self.p} \n   Product Price ={self.pr} \n")

p_lst = []
pr_lst = []
A = "yes"
c = 0

while A =="yes" or A=="Yes" or A=="YES":
    c+=1
    p =input("Product Name :")
    pr =input("Product Price :")
    p_lst.append(p)
    pr_lst.append(pr)
    A = input("Add Another item ?[yes / no]:")
    
for i in range(c):
    p_name = p_lst[i]
    price = pr_lst[i]
    D = Product(i+1,p_name,price)
    D.Display()

    
