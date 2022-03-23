from cmath import sqrt
import operator
import numpy as np
from PIL import Image
from numpy import asarray
from math import *

import glob

sunfile = glob.glob("/home/nahid/Documents/desert/*")
moonfile = glob.glob("/home/nahid/Documents/Snow/*")


newimg = Image.open("/home/nahid/Documents/6.jpg")

#img  = Image
newimg.resize((200,200))

# .open("/home/nahid/Downloads/sun/sun1.jpeg")



newa = asarray(newimg)
newa = np.reshape(newa, (np.product(newa.shape),)) 


dr = list()
for file in sunfile: 
    img = Image.open(file)
    img.resize((200,200))
    suna = asarray(img)
    suna = np.reshape(suna, (np.product(suna.shape),))
    #x = getmin(len(suna), len(newa))
    dis = 0
    for i in range(400):
        dis += (newa[i] - suna[i])**2
    dis = sqrt(dis)
    dr.append([dis,"desert"])

   


for file in moonfile: 
    img = Image.open(file)
    img.resize((200,200))
    
    moona = asarray(img)
    moona = np.reshape(moona, (np.product(moona.shape),))
    
    #x = getmin(len(moona), len(newa))
    dis = 0
    for i in range(400):
        dis += (newa[i] - moona[i])**2
    dis = sqrt(dis)
    dr.append([dis,"snow"])


dr = sorted(dr, key=lambda x: x[0])
for dis in dr:
    print(dis)

k = 3
for dis in dr:
    print(dis[1])
    k-=1
    if(k==0):
        break

# print(dr)
