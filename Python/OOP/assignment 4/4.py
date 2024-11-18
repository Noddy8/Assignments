class table : 
    def mult(self , n ):
        n = n
        i = 1
        while i < 11:
            print(f"{n} x {i} = {n*i}")
            i+=1

    def all(self):
        for i in range(1 , 10):
            for j in range(1 , 11):
                print(f"{i} x {j} = {i*j}")
            print(f"\n**************************\n")

t1 = table()
t1.mult(3)
t1.all()