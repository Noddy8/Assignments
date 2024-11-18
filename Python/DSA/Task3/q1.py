def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

num_terms = int(input("Enter the number of terms: "))
fibonacci(num_terms)
