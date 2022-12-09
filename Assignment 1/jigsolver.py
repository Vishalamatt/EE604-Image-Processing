#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import numpy as np
from PIL import Image,ImageOps
im = Image.open(sys.argv[1])

#image 1 cropping and changing G and B values
im1 = im.crop((0,0,190,200))
image = np.array(im1)
image = image[:, :, [0,2,1]]
im11 = Image.fromarray(image)

#image 2 cropping nd flipping
im2 = im.crop((0,200,190,410))
im22 = ImageOps.flip(im2)

#image 3 cropping and mirror
im3 = im.crop((515,150,700,330))
im33 = ImageOps.mirror(im3)

#image 4 cropping and flipping
im4 = im.crop((370,370,797,421))
im44 = ImageOps.flip(im4)

im.paste(im11,(0,200))
im.paste(im22,(0,0))
im.paste(im33,(515,150))
im.paste(im44,(370,370))

#padding, by copying pixels 5 pixels from above and 5 from below
padd = np.array(im)
for i in range(5):
  padd[400+i,0:190:,:] = padd[399-i,0:190,:]
for i in range(5):
  padd[405+i,0:190,:] = padd[414-i,0:190,:]

#final image code
final = Image.fromarray(padd)
final.show()
final.save("final.jpg")


# In[ ]:




