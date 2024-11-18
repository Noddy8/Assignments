#Ex-7 : read and Overwrite .
f = open('7.txt','r')
print(f.read())
f.close()

f = open('7.txt','w')
f.write('\n This line is overwrite.')
f.close()


