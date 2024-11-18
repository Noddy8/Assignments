class computation:

    def __init__(self):
        pass

    def sum(self , n):
        n = n + 1
        i = 1
        sum = 0
        while i < n:
            sum += i
            i += 1

        return sum

    def factorial(self , n):
        n = n + 1
        i = 1
        total = 1
        while i < n:
            total = total * i
            i += 1

        return total

obj = computation()
print(f"sum = {obj.sum(5)}")
print(f"factorial = {obj.factorial(5)}")
