#Q4.
myLst = [1, "A", 'MSU', 123, 909, 78.88, 77, 6544, 78.50, 7+9j, True, False, 900000, "XYZ", 90.99999999999]
print(myLst)
print(myLst[6])
print(myLst[-2])
print(myLst[-10])
print(myLst[0:6])
print(myLst[1:6])
print(myLst[6:10])
print(myLst[:])
print(myLst[::])
print(myLst[::-1])
print(myLst[:10])
print(myLst[::2])
print(myLst[0::1])
print(myLst[2:13:4])
#Q5.Delete an item from the list.
myLst.remove("XYZ")
print(myLst)
myLst.pop(2)
print(myLst)
#Q6.Delete elements available at odd indices from the list.
del myLst[1: :2]
print(myLst)
#Q7.Delete elements available at even indices from the list.
del myLst[0: :2]
print(myLst)
#Q8.Delete the definition of the list.
del myLst
print(myLst)
