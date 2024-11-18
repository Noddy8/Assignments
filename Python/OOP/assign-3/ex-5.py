#EX-5 . Average:

class Test:
    def average():
        a = Test.num()
        s = 0
        for j in range(len(a)):
            s = s + a[j]
            ans = s / len(a)
        return  ans
    
    def display():
        return f'Average is {Test.average()}'

    def num():
        n = int(input(f"How many numbers :"))
        print()
        lst =[]
        for i in range(n):
            no = float(input(f"Number-{i+1} :"))
            lst.append(no)
        return lst
    
print(Test.display())
