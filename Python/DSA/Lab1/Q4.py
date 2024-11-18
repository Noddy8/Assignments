#Write a program to multiply two numbers without * operator.

n=int(input('enter num1:'))
m=int(input('enter num2:s'))
l=0
while m>0:
    l+=n
    m-=1
print(l)