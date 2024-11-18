#ex-3. program to add movie details by constructor in list and print :

class Movie:
    def __init__(self,n,h,hn):
        self.n = n
        self.h = h
        self.hn = hn
    def info(self):
        print(f"Movie Name : {self.n} ")
        print(f"Hero Name : {self.h}")
        print(f"Heroine Name : {self.hn}")
lst = []
while True :
    n = input("Enter Movie Name : ")
    h = input("Enter Hero Name : ")
    hn = input("Enter Heroine Name : ")
    m = Movie(n,h,hn)
    lst.append(m)
    print("------Movie Added Successfully------")
    o = input("If Add another Movie ,Enter [Yes] :")
    if o=="Yes" or o=="yes":
        pass
    else:
        break
print('All movies information:')
for movie in lst:
	movie.info()
	print()
	 

    