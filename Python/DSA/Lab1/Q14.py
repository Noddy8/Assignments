#Write a program to find greatest of 3 numbers.
a=int(input('Enter num1:'))
b=int(input('Enter num2:'))
c=int(input('Enter num3:'))
if b<a>c:
    print('Greatest number is num1:',a)
elif a<b>c:
    print('Greatest number is num2',b)
elif b<c>a:
    print('Greatest number is num3',c)
else:
    print('All are Equal number.')