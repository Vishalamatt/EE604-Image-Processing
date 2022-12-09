#!/usr/bin/env python
# coding: utf-8

# In[39]:


import sys
import numpy as np
import cv2 as cv

# defining gamma function
def gammaCorrection(src, gamma_value):
    inverse_gamma = 1 / gamma_value

    t_list = [((i / 255) ** inverse_gamma) * 255 for i in range(256)]
    t_list = np.array(t_list, np.uint8)

    return cv.LUT(src, t_list)

# cctv1
img = cv.imread(str(sys.argv[1]))

if "cctv1" in str(sys.argv[1]) :
    R,G,B = cv.split(img)
    outr = cv.equalizeHist(R)
    outg = cv.equalizeHist(G)
    outb = cv.equalizeHist(B)
    out = cv.merge((outr,outg,outb))
    cv.imwrite('enhanced-cctv1.jpg',out)

# cctv2
if "cctv2" in str(sys.argv[1]) :
    image = gammaCorrection(img, 1.3)
    cv.imwrite('enhanced-cctv2.jpg',image)
    
# cctv3
if "cctv3" in str(sys.argv[1]) :
    imgn = gammaCorrection(img, 2)
    R,G,B = cv.split(imgn)
    outr = cv.equalizeHist(R)
    outg = cv.equalizeHist(G)
    outb = cv.equalizeHist(B)
    out = cv.merge((outr,outg,outb))
    cv.imwrite('enhanced-cctv3.jpg',out)

# cctv4
if "cctv4" in str(sys.argv[1]) :
    imgn = gammaCorrection(img, 0.6)
    R,G,B = cv.split(imgn)
    outr = cv.equalizeHist(R)
    outg = cv.equalizeHist(G)
    outb = cv.equalizeHist(B)
    out = cv.merge((outr,outg,outb))
    cv.imwrite('enhanced-cctv4.jpg',out)


# In[ ]:




