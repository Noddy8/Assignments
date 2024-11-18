#Ex-8.
class Student:
    def __init__(sn,Name,Marks):
        sn.n = Name
        sn.m = Marks

    def Display(sn):
        print("---Detailes---")
        print(f' Name : {sn.n} \n Marks : {sn.m}')

def grade(sn):
    if sn=="ram":
        return f' Grad of Ram is first.'
    elif sn=="meet":
        return ' Grad of Meet is Second.'
    elif sn =="om":
        return " Grad of Om is Third."
    else:
        return " Syam is Fail."
def get__():
    sn = input("Name : ")
    if sn=="ram":
        ram.Display()
        print(grade("ram"))
    elif sn=="meet":
        meet.Display()
        print(grade("meet"))
    elif sn =="om":
        om.Display()
        print(grade("om"))
    elif sn=="syam":
        syam.Display()
        print(grade("syam"))
    else:
        print("---Enter Appropriate Name---")
        return get__()

om = Student("Om",'70')
meet = Student("Meet",'75')
syam = Student("Syam",'30')
ram = Student("Ram",'90')
get__()
