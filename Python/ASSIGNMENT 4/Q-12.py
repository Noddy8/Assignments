# Program to count total number of notes of  denomination 50,100,500,2000 Rupees in given amount.
Amt = int(input("Enter the Amount: "))
if Amt<2000:
    print("Amount should be more than 2000")
else:
    fifty= Amt/50
    hundred= Amt/100
    twoHundred= Amt/200
    fiveHundred= Amt/500
    twoThousand= Amt/2000
    
    print(f"Number of required 50 Notes = {fifty} \nNumber of required 100 Notes = {hundred}\nNumber of required 200 Notes = {twoHundred} \nNumber of required 500 Notes = {fiveHundred} \nNumber of required 2000 Notes = {twoThousand}")