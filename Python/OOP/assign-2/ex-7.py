#EX-7. Test class.
class Test: 
    def __init__(self): 
        self.a=10 
        self.b=20 
t1=Test()
t2=Test()
t1.a =111
t1.b =222
print(f' t1.a ={t1.a} ;t1.b ={t1.b} \n t2.a ={t2.a} , t2.b ={t2.b}')
print("ID of t1 =",id(t1))
print("ID of t2 =",id(t2))
