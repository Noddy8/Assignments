#Ex-8.
class Student:
    def __init__(sn,Name,Marks):
        sn.n = Name
        sn.m = Marks

    def Display(sn):
        print("---Detailes---")
        print(f'\n Name : {sn.n} \n Marks : {sn.m}')

    def grade(sn):
        if sn.m>=90:
            return f' Grad of {sn.n} is first.'
        elif sn.m>=70:
            return f' Grad of {sn.n} is Second.'
        elif sn.m >=40:
            return f" Grad of {sn.n} is Third."
        else:
            return f" {sn.n} is Fail."
def get__():
    name = input("Name :")
    Marks = float(input("Marks :"))
    SD = Student(name,Marks)
    SD.Display()
    print(SD.grade())
    RE = input(f"\nRetry? [yes / no] :")
    if RE =="yes":
        return get__()
get__()
