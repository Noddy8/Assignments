'''Write a program to print the name, age, height in meter and weight in KG of a person in single line (Hint: Use multiple Assignment), print this information on the screen and also calculate the BMI and decide whether the person is healthy or unhealthy.
BMI= weight (kg) / [height (m)]2
• If your BMI is less than 18.5, it falls within the underweight range.
• If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
• If your BMI is 25.0 to 29.9, it falls within the overweight range.
• If your BMI is 30.0 or higher, it falls within the obese range.
'''
name, age, height, weight = "John Smith", 30, 1.8, 80
bmi = weight / (height ** 2)

print(f"Name: {name}, Age: {age}, Height: {height}m, Weight: {weight}kg")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Healthy weight")
elif 25.0 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")