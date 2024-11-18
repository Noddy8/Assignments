#Ex-1. properties of file.

f = open('1.txt','w')
print('File Name :',f.name)
print('File Mode :',f.mode)
print('Is File Readable? :',f.readable())
print('Is File writable? :',f.writable())
print('Is File Closed? :',f.closed)
f.close()
print('Is File Closed? :',f.closed)
