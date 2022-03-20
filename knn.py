from cmath import sqrt
import operator
import numpy as np
from PIL import Image
from numpy import asarray
from math import *

import glob

sunfile = glob.glob("/home/nahid/Downloads/sun/*")
moonfile = glob.glob("/home/nahid/Downloads/moon/*")

newimg = Image.open("/home/nahid/Downloads/night.jpeg")
img  = Image.open("/home/nahid/Downloads/sun/sun1.jpeg")


newa = asarray(newimg)
newa = np.reshape(newa, (np.product(newa.shape),)) 

def getmin(a,b):
    if(a>b):
         return b
    else:
         return a
    
dr = list()
for file in sunfile: 
    img = Image.open(file)
    suna = asarray(img)
    suna = np.reshape(suna, (np.product(suna.shape),))
    x = getmin(len(suna), len(newa))
    dis = 0
    for i in range(x):
        dis += (newa[i] - suna[i])**2
    dis = sqrt(dis)
    dr.append([dis,"sun"])


for file in moonfile: 
    img = Image.open(file)
    moona = asarray(img)
    moona = np.reshape(moona, (np.product(moona.shape),))
    x = getmin(len(moona), len(newa))
    dis = 0
    for i in range(x):
        dis += (newa[i] - moona[i])**2
    dis = sqrt(dis)
    dr.append([dis,"moon"])




dr = sorted(dr, key=lambda x: x[0])
for dis in dr:
    print(dis)

k = 3
for i in range(k):
    
# print(dr)
