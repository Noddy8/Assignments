import os

f = open("C:/Users/15hem/OneDrive/Desktop/hanuman-wallpaper.png",'rb')
fn = open('image.jpg','wb')
fn.write(f.read())
print('Image is copied Successfully.')
f.close()
fn.close()
