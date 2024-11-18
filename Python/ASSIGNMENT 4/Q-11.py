# Program to check if the input year is a leap year or not.
'''Note: Divided by 100 means century year (ending with 00)  # century year divided by 400 is leap year
Not divided by 100 means not a century year 
Year divided by 4 is a leap year 
If not divided by both 400 (century year) and 4 (not century year) year is not leap year'''
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year". format(year))                                          
else:                                                                                                             
    print ("{0} is not a leap year". format (year))