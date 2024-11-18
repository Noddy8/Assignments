#Write a program which multiplies a number with two without the number*2 operation.

n=int(input('enter num1:'))
m=2
l=0
while m>0:
    l+=n
    m-=1
print(l)
