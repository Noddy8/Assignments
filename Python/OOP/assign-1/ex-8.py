#8. Write a Python program to create an Employee class :

class Employee:
    
    #Use constructor to store name,no and department.
    def __init__(self,name,empno,empdept):
        self.name = name
        self.empno = empno
        self.empdept = empdept

    def Emp_detail(self):
        return f' Name        : {self.name} \n Employee_no : {self.empno} \n Emp_dept    : {self.empdept}'


mahesh = Employee("Mahesh",1,"Finance Dept")
ramesh = Employee("Ramesh",2,"Marketing Dept")

print(mahesh.Emp_detail())
