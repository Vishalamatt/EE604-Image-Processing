#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
from PIL import Image, ImageDraw
#n = int(input())
im = Image.new('RGB', (500, 300), (0,0,0))
draw = ImageDraw.Draw(im)
d = int(sys.argv[1])
r=0
for x in range(2):
    n= int(d)
    if d>9:
        n= int(d/10)
        d = d%10

    if x==1:
        r=250
    if n==0:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((40+r, 185, 90+r, 235), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==1:
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 65, 150+r, 115), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 185, 150+r, 235), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255)) 

    if n==2:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((40+r, 185, 90+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))
    if n==3:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==4:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))
    if n==5:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==6:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 185, 90+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==7:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==8:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 185, 90+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

    if n==9:
        draw.ellipse((40+r, 5, 90+r, 55), fill=(255, 255, 255))
        draw.ellipse((100+r, 5, 150+r, 55), fill=(255, 255, 255))
        draw.ellipse((160+r, 5, 210+r, 55), fill=(255, 255, 255))
        draw.ellipse((40+r, 65, 90+r, 115), fill=(255, 255, 255))
        draw.ellipse((160+r, 65, 210+r, 115), fill=(255, 255, 255))
        draw.ellipse((40+r, 125, 90+r, 175), fill=(255, 255, 255))
        draw.ellipse((100+r, 125, 150+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 125, 210+r, 175), fill=(255, 255, 255))
        draw.ellipse((160+r, 185, 210+r, 235), fill=(255, 255, 255))
        draw.ellipse((40+r, 245, 90+r, 295), fill=(255, 255, 255))
        draw.ellipse((100+r, 245, 150+r, 295), fill=(255, 255, 255))
        draw.ellipse((160+r, 245, 210+r, 295), fill=(255, 255, 255))

im.save("final.jpg")


# In[ ]:





# In[ ]:




