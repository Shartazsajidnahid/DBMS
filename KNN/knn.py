from cmath import sqrt
from hashlib import new
import operator
import numpy as np
from PIL import Image
from numpy import asarray
from math import *

import glob

sunfile = glob.glob("/home/nahid/Documents/desert/*")
moonfile = glob.glob("/home/nahid/Documents/Snow/*")


newimg = Image.open("/home/nahid/Documents/4.jpg")
newimg.show()

#img  = Image
newimg.resize((300,300))

newa = asarray(newimg)
newa = np.reshape(newa, (np.product(newa.shape),)) 
# newimg_data = newimg.getdata()
# newa = np.array(newimg_data)
# newa = newa.flatten()

dr = list()

def calc_distance(img,type):
    # print("hey")
    img.resize((300,300))
    sunimg = img.getdata()
    suna = np.array(sunimg)
    suna = suna.flatten()
    #x = getmin(len(suna), len(newa))
    dis = 0
    for i in range(400):
        dis += (newa[i] - suna[i])**2
    dis = sqrt(dis)
    dr.append([dis,type])



for file in sunfile: 
    img = Image.open(file)
    calc_distance(img,'desert')

  

for file in moonfile: 
    img = Image.open(file)
    calc_distance(img,'snow')
    


dr = sorted(dr, key=lambda x: x[0])
for dis in dr:
    print(dis)

k = 3
n_sun = 0
n_moon = 0

for dis in dr:
    #print(dis[1])
    if(dis[1]=='desert'):
        n_sun+=1
    else:
        n_moon+=1
    k-=1
    if(k==0):
        break

if(n_sun>n_moon):
    print("The image is a Desert type")
else: 
    print("The image is a Snow type")

# print(dr)
