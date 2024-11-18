#Program performing slice operation on strings
string= "Python is Easy !!!"
print(string)
print(string[0])
print(string[: :-1])
print(string[:])
print(string[-3])
print(string[3: 9])
print(string[ : 5])
print(string[0:])
print(string*2)
print(string+ "Isn\'t it")
print(string[0:])
'''
string[3] = "X" ''' #Will give a Error: 'str' object does not support item assignment
# So correcting it:
string= string[:3] +"X" + string[4:]
print(string)
# OR

str_list= list(string)
str_list[3]="H"
strN= "".join(str_list)
print(strN)
