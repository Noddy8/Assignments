#11-(i).testing..

class Test:
    a=10  # a is static variable
    def  __init__(self):
        self.b=20 # b is instance variable
t1=Test()
t2=Test()
Test.a=888
Test.b=999
print('t1:' , t1.a,t1.b)
print('t2:' , t2.a,t2.b)
