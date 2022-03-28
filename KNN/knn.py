from cmath import sqrt
from hashlib import new
import operator
import numpy as np
from PIL import Image
from numpy import asarray
from math import *

import glob

desertfile = glob.glob("/home/nahid/Documents/desert/*")
snowfile = glob.glob("/home/nahid/Documents/Snow/*")


newimg = Image.open("/home/nahid/Documents/4.jpg")
# newimg.show()

#img  = Image
newimg.resize((300,300))

# newarr = asarray(newimg)
# newarr = np.reshape(newarr, (np.product(newarr.shape),)) 
newimg_data = newimg.getdata()
newarr = np.array(newimg_data)
newarr = newarr.flatten()

dr = list()

def getarr(img):
    img.resize((300,300))
    img_data = img.getdata()
    img_arr = np.array(img_data)
    img_arr = img_arr.flatten()
    return img_arr

def calc_min(img):
    global minlen
    # print("hey")
    img_arr = getarr(img)
    if(len(img_arr)<minlen):
        minlen = len(img_arr)
    

def calc_distance(img,type):
    global minlen
    # print("hey")
    img_arr = getarr(img)
    #x = getmin(len(suna), len(newa))
    dis = 0
    for i in range(minlen):
        dis += (newarr[i] - img_arr[i])**2
    dis = sqrt(dis)
    dr.append([dis,type])

#calculate min length
minlen = int(1000000000)
for file in desertfile: 
    img = Image.open(file)
    calc_min(img)

for file in snowfile: 
    img = Image.open(file)
    calc_min(img)

minlen = min(minlen,len(newarr))


#calclulate distance
for file in desertfile: 
    img = Image.open(file)
    calc_distance(img,'desert')


for file in snowfile: 
    img = Image.open(file)
    calc_distance(img,'snow')
    


dr = sorted(dr, key=lambda x: x[0])
# for dis in dr:
#     print(dis)

k = 3
n_desert = 0
n_snow = 0

for dis in dr:
    #print(dis[1])
    if(dis[1]=='desert'):
        n_desert+=1
    else:
        n_snow+=1
    k-=1
    if(k==0):
        break

if(n_desert>n_snow):
    print("The image is a Desert type")
else: 
    print("The image is a Snow type")

# print(dr)
