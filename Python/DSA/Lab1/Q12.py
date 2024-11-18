#Write a program to check -ve, +ve or 0.
a=int(input('Enter a num:'))
if a==0:
    print('Number entered is 0')
else :
    if a<0:
        print('NUmber entered is negative')
    if a>0:
        print('Number entered is positive')