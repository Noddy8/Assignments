#Ex-4. Create a file and Display the Content:

f = open('4.txt','w')
f.write("This is 4th Example.")
f.close()
f = open('4.txt','r')
print(f.read())
f.close()
