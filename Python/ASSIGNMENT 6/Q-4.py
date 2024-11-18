i = 0
while i <=2:
    x = int(input("Enter a number:"))
    if x == 99:
        print("Congratulations:")
        i = i + 2
    elif x < 99:
        print("Enter higer number!")
    else:
        print("Enter lower number:")