#7. Write a Python program to create a Student class :

class student:
    # Create one no arg constructor to print welcome.
    def __init__(self):
        print("---Hello---")
        print("")


    # Create a function to display student's information :

    def studinfo(self):
     return f" Name      : {self.name} \n Roll no   : {self.Roll_no} \n cotact no : {self.contactnum}."

#Type = 1:

def choosename():
    a =input("Student Name :")
    if a=="hemang":
        hemang = student()
        hemang.name = "Hemu"
        hemang.Roll_no = 34
        hemang.contactnum = 9994447770
        print(hemang.studinfo())

    elif a=="chetan":
        chetan = student()
        chetan.name = "Chetan"
        chetan.contactnum = 9999888776
        chetan.Roll_no = 19
        print(chetan.studinfo())

    elif a=="amar":
        amar = student()

        amar.name = "Amar"
        amar.Roll_no = 13
        amar.contactnum = 3777555888
        print(amar.studinfo())

    else :
        print("Enter the name properly.")
        return choosename()
choosename()

#type = 2 :
'''
hemang = student()
chetan = student()
amar = student()

hemang.name = "Hemu"
hemang.Roll_no = 34
hemang.contactnum = 9994447770

chetan.name = "Chetan"
chetan.contactnum = 9999888776
chetan.Roll_no = 19

amar.name = "Amar"
amar.Roll_no = 13
amar.contactnum = 3777555888

print(amar.studinfo())
'''



