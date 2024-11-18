import os

f= open('3.txt','w')
print('Is file Created ? :',os.path.exists('3.txt'))
f.close()
