#Write a program to swap two numbers using a third variable.
a=int(input('Enter num1:'))
b=int(input('Enter num2:'))
print('before swaping num1', a)
print('after swaping num2',b)
t=a
a=b
b=t
print('after swaping num1:',a)
print('after swaping num2:',b)