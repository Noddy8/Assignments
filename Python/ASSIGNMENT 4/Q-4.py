#Write a program to find the largest of given two numbers.
num1 = int(input("Enter first number: "))      
num2 = int(input("Enter second number: ")) 

if num1 >= num2:   
     if num1 == num2:    
         print("Both numbers are equal.")       
     else:  
         print("Fisrt number is greater than the second number.")
else:   
     print("Second number is greater than the First number.") 
