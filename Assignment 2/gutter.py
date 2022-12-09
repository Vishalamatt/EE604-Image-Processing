#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np
import sys
import cv2 

# defining gamma function
def gammaCorrection(src, gamma_value):
    inverse_gamma = 1 / gamma_value

    t_list = [((i / 255) ** inverse_gamma) * 255 for i in range(256)]
    t_list = np.array(t_list, np.uint8)

    return cv2.LUT(src, t_list)

img = cv2.imread(str(sys.argv[1]))

# gutter 1
if "gutters1" in str(sys.argv[1]) :
    crop = img[0:777,0:110]
    img1 = gammaCorrection(crop, 1.9)
    img[0:777,0:110] = img1
    cv2.imwrite('cleaned-gutter1.jpg',img)
    
# gutter 2
if "gutters2" in str(sys.argv[1]) :
    crop = img[0:935,525:625]
    img1 = gammaCorrection(crop, 1.9)
    img[0:935,525:625] = img1
    cv2.imwrite('cleaned-gutter2.jpg',img)

# gutter 3
if "gutters3" in str(sys.argv[1]) :
    img = gammaCorrection(img, 3)
    cv2.imwrite('cleaned-gutter3.jpg', img)


# In[ ]:




