#Ex-16. Check Number is a Palindrome or Not.
try:
    mn = int(input("Enter The Number :"))
    mn = str(mn)
    f = open('Number.txt','w')
    f.write(mn)
    f.close()
    f = open('Number.txt','r')
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
    
except Exception as e:
    print(e)



