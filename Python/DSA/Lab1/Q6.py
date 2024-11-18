#Write a program which performs the integer division on a number with two without the number/2 operation.

d=int(input('Enter Num1:'))
f=int(input('Enter Num2:'))
a=0
while d>=f:
    a+=1
    d-=f
print(a)
