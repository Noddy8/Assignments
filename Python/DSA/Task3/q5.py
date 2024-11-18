def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for char in num_str:
        sum += int(char) ** num_len
    return sum == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
