#9. program to create factorial function using recursion.


def factorial(n):
    if n==1:
        return 1
    
    elif n==0:
        return 0

    else :
        #return the factorial function as recursion.
        return n*factorial(n-1)
n =int(input("num :"))
print(factorial(n))    

 
