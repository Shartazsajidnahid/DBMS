from cmath import sqrt
import operator
import numpy as np
from PIL import Image
from numpy import asarray
from math import *

import glob

sunfile = glob.glob("/home/nahid/Downloads/sun/*")
moonfile = glob.glob("/home/nahid/Downloads/moon/*")


newimg = Image.open("/home/nahid/Downloads/newmoon.jpeg")
newimg.show()

#img  = Image
newimg.resize((200,200))

# .open("/home/nahid/Downloads/sun/sun1.jpeg")



newa = asarray(newimg)
newa = np.reshape(newa, (np.product(newa.shape),)) 


dr = list()
for file in sunfile: 
    img = Image.open(file)
    img.resize((200,200))
    sunimg = img.getdata()
    suna = np.array(sunimg)
    suna = suna.flatten()
    #x = getmin(len(suna), len(newa))
    dis = 0
    for i in range(400):
        dis += (newa[i] - suna[i])**2
    dis = sqrt(dis)
    dr.append([dis,"sun"])

  

for file in moonfile: 
    img = Image.open(file)
    img.resize((200,200))
    
    moonimg = img.getdata()
    moona = np.array(moonimg)
    moona = moona.flatten()
    
    #x = getmin(len(moona), len(newa))
    dis = 0
    for i in range(400):
        dis += (newa[i] - moona[i])**2
    dis = sqrt(dis)
    dr.append([dis,"moon"])


dr = sorted(dr, key=lambda x: x[0])
for dis in dr:
    print(dis)

k = 3
n_sun = 0
n_moon = 0

for dis in dr:
    #print(dis[1])
    if(dis[1]=='sun'):
        n_sun+=1
    else:
        n_moon+=1
    k-=1
    if(k==0):
        break

if(n_sun>n_moon):
    print("The image is a sun type")
else: 
    print("The image is a moon type")


# print(dr)
