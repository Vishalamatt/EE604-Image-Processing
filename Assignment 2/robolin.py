#!/usr/bin/env python
# coding: utf-8

# In[33]:


import cv2
import sys
import numpy as np
 
image = cv2.imread(str(sys.argv[1]))
 
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# canny edge detection method
lower_t = 120
upper_t = 180
edges = cv2.Canny(gray_image,lower_t,upper_t)
 
# Apply probablistic houghlines method to  obtain line
linelist =[]
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=5, maxLineGap=10)
 
# Iteration
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    # draw the lines joing the points over original image
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    linelist.append([(x1,y1),(x2,y2)])
     
# Save the result image with original image name
name = 'robolin-' + str(sys.argv[1])
cv2.imwrite(name, image)


# In[ ]:




