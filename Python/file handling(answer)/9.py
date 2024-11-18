#Ex-9:
f = open('file1.txt','w')
s = input("Enter the String :")
f.write(s)
f.close()

f = open('file1.txt','r')
print(f.read())
f.close()

f = open('file1.txt','w')
f.seek("Worship")
f.write("Mandatory")
f.close()
