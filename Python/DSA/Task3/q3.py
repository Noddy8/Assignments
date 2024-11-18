def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = find_largest(num1, num2, num3)
print(f"Largest of {num1}, {num2} and {num3} is: {largest}")
