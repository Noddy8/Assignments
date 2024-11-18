#EX-5. Test Class

class Test: 
    def __init__(self): 
        self.a=10 
        self.b=20 
        self.c=30 
        self.d=40 
    def m1(self): 
        del self.d 
t1= Test()
print(t1.a,t1.b,t1.c,t1.d)
t1.m1()
print(t1.a,t1.b,t1.c)
del t1.c
dic = {"t1.a":t1.a,"t1.b":t1.b}
print(dic) 
