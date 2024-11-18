number = int(input("Enter Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

for i in range(1, number + 1):
    if(i != number):
        print("%d^2 + " %i, end = ' ')
    else:
        print("{0}^2 = {1}".format(i, total))
        