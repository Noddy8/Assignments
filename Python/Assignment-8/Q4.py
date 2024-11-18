#Q4.Create a list that is populated with all the even numbers between 1-1000.
Newlist = []
for x  in range(1,1000):
   if x % 2 == 0:
      Newlist.append(x)      
print(Newlist) 
