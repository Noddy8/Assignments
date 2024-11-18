#EX = 13. check number of lines, words and characters in the file:
import os

fname = input("File Name :")+'.txt'
if os.path.isfile(fname):
    lines = 0
    words = 0
    chars = 0
    f = open(fname,'r')
    for l in f:
        lines += 1
        w = l.split()
        words += len(w)
        l = l.strip('\n')
        chars += len(l)
    print('No of lines     :',lines)
    print('No of words     :',words)
    print('No of characters:',chars)
else:
    print("File is Not Exists.")
