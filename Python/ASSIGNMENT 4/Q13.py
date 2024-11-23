'''Program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Print Fail Message'''
print("Enter your marks out of 100, as per the subject asked...")
Physics = (int(input("Physics: ")))
Chemistry = (int(input("Chemistry: ")))
Biology = (int(input("Biology: ")))
Mathematics = (int(input("Mathematics: ")))
Computer = (int(input("Computer: ")))

total = Physics + Chemistry + Biology + Mathematics + Computer
Percentage = total/500*100
print("Percentage =",Percentage)
if Percentage >= 90 and Percentage < 100: 
    print("Grade A")
elif Percentage >= 80 and Percentage < 100: 
    print("Grade B")
elif Percentage >= 70 and Percentage < 100: 
    print("Grade C")
elif Percentage >= 60 and Percentage < 100: 
    print("Grade D")
elif Percentage >= 40 and Percentage < 100: 
    print("Grade E")
elif Percentage < 40 and Percentage < 100: 
    print("You are Failed,Try next time.")
else:
    print("Enter vaild Marks...!")