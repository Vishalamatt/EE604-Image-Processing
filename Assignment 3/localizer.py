import cv2
import numpy as np
import sys

# import the image and read it as argument
img1 = cv2.imread(str(sys.argv[1]))
img = np.array(img1)

# By using the hint from the research papaer about the absolute difference between
# different color channels and then using the range of those absolute difference 
# we can get the desired results, first we calculate the two (G-B) and (2G-B-R) 
# absolute difference and then we put if conditions for the range to classify them
# as either road, building or grass
sum = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img[i][j][:]
        d = abs(int(a[2])-int(a[1]))
        sum += d

y = 65*87
m1 = sum/y
               
sum = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img[i][j][:]
        d = abs(2*int(a[1])-int(a[2])-int(a[0]) )
        sum += d

y = 65*87
m2 = sum/y               

# using the ranges given in the paper, refer to the paper for the range values
if m1<=80 and m2<=85 and m2>=12:
    print("2")

if m1<=6 and m2<=8 and m2>=1:
    print("1")
    
if m1>6 and m1<=20 and m2<12:
    print("3")               
               
               
               
               
               
               
               
               
               
               
               
               
               
  