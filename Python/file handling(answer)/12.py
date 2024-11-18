import os
g = input("Enter the File Name :")+'.txt'
if os.path.isfile(g):
    print('File exists',g)
    f=open(g,'r')
    print('Content of file is :',end=' ')
    print(f.read())
else:
    print('File doesn’t exist')
