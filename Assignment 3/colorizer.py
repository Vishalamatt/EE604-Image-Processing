import cv2
import numpy as np
import sys

# read all the images as arguments
# 1,2,3 are the arguments corresponding to Y,Cb,Cr 
Y = cv2.imread(str(sys.argv[1]))
imgcb = cv2.imread(str(sys.argv[2]))
imgcr = cv2.imread(str(sys.argv[3]))

# first we resize the image to make the Cb and Cr channels size equal to the Y size, that is (622,960)
cb = cv2.resize(imgcb, (960,622))
cr = cv2.resize(imgcr, (960,622))

# Now, since the image itself have 3 channels having same values as other 2 channels 
# we can paste the vales of Cb and Cr channel in 2nd and 3rd channel of Y image 
# so to make it an full YCbCr image 

# for Cb pasting
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        Y[i][j][1] = cb[i][j][0]

# for Cr pasting
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        Y[i][j][2] = cr[i][j][0]
        
# conversion to BGR 
img_bgr = cv2.cvtColor(Y, cv2.COLOR_YCrCb2RGB)

# since opencv saves as BGR rather than RGB, we already made the image as BGR so it will have 
# opposite effect and hence we get the RGB image as saved one
cv2.imwrite('flyingelephant.jpg',img_bgr)