# Program to check whether the given number is between 1 and 100 or not.

def main():
    
    try:
        x = int(input("type a number : "))
    except (ValueError):
        print("Vaild Integer Required.")
        main()


    if x >= 1 and x <= 100 :
        print("The number" , x ,"is between 1 to 100 .")
        main() 
    else :
        print("The number" , x ,"is not between 1 to 100 .") #Loop ends if x > 100
main()
        
