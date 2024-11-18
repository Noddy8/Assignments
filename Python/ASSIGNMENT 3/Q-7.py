
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[::])
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[0])
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:3])
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[2:])
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst*2)

 #Add one item to a list using append() function 
my_list = [50, 70, 30, 20, 90, 10, 50]
another_list = [5, 7, 3, 2, 9, 1, 5]
my_list.extend(another_list)         #Add several items to the list using extend() function	
print (my_list)


#Changing 2nd to 4th items in the list
List=[50, 70, 30, 20, 90, 10, 50]
print("original list ")
print(List)

List[2] = 11

List[4] = 21
print("New list")
print(List)

#Using insert() function
list=[1,9]
list.insert(1,3)
print(list)
list[2:2]=[5,7]
print(list)

#Deleting the entire list
del list
print(list)	#Error would be generated because it no more exists

#Removing a given item from the list
list=['p','q','r','s','m']  
list.remove('p')
print(list)

#Pop() method is used to remove an item at the given index
list.pop(1)	#Removes the item at the given index
list.pop()	#Removes the last item if the index is not provided

#Clear() method to empty the whole list 
list.clear()
print(list)

#index() method : returns the index of the first matched item/first occurence
list=[7,8,12,15,96]  
list.index(8) #Output: 1

#sort() method : sort items in a list in ascending order
list=[12,44,85,96,25,36]
print(List.sort())

#reverse() method : reverse the order of items in the list
print(list.reverse())