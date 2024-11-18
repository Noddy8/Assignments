#EX-5. check whether the string is palindrome or not.

mn = input("Enter The Number :")
f = open('Test.txt','w')
f.write(mn)
f.close()
f = open('Test.txt','r')
a = f.read()
f.close()

l = len(a)
count = l//2
w = 0
for i in range(count):
    if a[i]==a[-(i+1)]:
        pass
    else:
        w +=1
if w>0:
    print(a,"isn't Palindrome Number.")
else:
    print(a,"is Palindrome Number.")
    
