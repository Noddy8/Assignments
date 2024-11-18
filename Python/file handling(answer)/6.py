#Ex-6 :  copy the contents of one file into another.

f = open('6.txt','r')
new_f = open('new-6.txt','w')
new_f.write(f.read())
f.close()
new_f.close()
