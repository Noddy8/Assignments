f = open('11.txt','a')
f.seek(int(input('New Pointer Location :')))
print(f.tell())
f.close()
