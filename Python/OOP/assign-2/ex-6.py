#Ex-6. Test Class
class Test:
    def __init__(self):
        self.a=10
        self.b=20 
        self.c=30 
        self.d=40 
t1=Test()
t2=Test()
del t1.a
print(t1.b,t1.c,t1.d)
print(t2.a,t2.b,t2.c,t2.d)
