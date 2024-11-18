#ex-4.
class Department:
    def __init__(self , dept_no):
        self.dno = dept_no
        
    def Dict_in(self):
        return f'   {dic}'

    def Display(self,dept_name):
        self.dname = dept_name
        
        
        return f'    Dept_No ={self.dno} \n    Dept_name ={self.dname}'
    def delete(self):
        del dept_name
        
dic = {}
c = 0
while True:
    c+=1
    dept_no = input("Department No :")
    dept_name = input("Department Name :")
    dt = Department(dept_no)
    dic["Name"] = dept_name
    dic["Dept No"] = dept_no
    r = input("Do you Want to add another [Yes/No] :")
    if r=="Yes" or r=="yes":
        pass
    else:
        break
    
del dept_no

for i in range(c):
    print(i+1,"1.  ",end="")
    print("------info in Dict------")
    print(dt.Dict_in())
    print()
    print(f'    ------Dept_info------')
    print(dt.Display(dept_name))
    print()
    print()
