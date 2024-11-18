#Ex-2. program to read/write multiple lines to the file.

f = open('2.txt','w')
f.write('hello students\n')
f.write('Python is a Higher Level Language.\n')
f.write('Bubyyye')
f.close()
f = open('2.txt','r')
print(f.read())
f.close()
