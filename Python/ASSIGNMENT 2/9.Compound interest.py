# Program to find Compound interest

p = float(input("Enter the princeple : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("Time in years     : ", t)


A=p*(1+r/100)**t
print ("Amount is",A)



ci=A-p

print("compound Interest : ", ci)

