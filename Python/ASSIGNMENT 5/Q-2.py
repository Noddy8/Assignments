# program to find the sum of the following series: 1 + 2 + 3 + …+ n

num = int(input("Enter a number: "))  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate until zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  