#Write a program to swap two numbers (without a third variable).
a=int(input('Enter num1:'))
b=int(input('Enter num2:'))
print('Before swaping num1:',a)
print('Before swaping num2:',b)
a,b=b,a
print('After swaping num1:',a)
print('After swaping num2:',b)