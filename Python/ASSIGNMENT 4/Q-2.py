# Program to print  no. Of days of Month. If you enter March as month then output should be like this : No of days of  “March” is : 31
month_name = input("Input the name of Month: ")

month_name = month_name.lower()

if month_name == "february":
	print("No. of days: 28/29 days")
	
elif month_name in ("april", "june", "september", "november"):
	print("No. of days: 30 days")
 
elif month_name in ("january", "march", "may", "july", "august", "october", "december"):
	print("No. of days: 31 day")
else:
	print("Please enter a vaild month name") 
	
