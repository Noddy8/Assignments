#ex-2 .program to evaluate an expression entered by the user.

exp = input("Enter the Expression :")
ans = eval(exp)
print(exp,"=",ans)

manually ="23+5*2"
print()
print("---Manually---")
print(manually,"=",eval(manually))

