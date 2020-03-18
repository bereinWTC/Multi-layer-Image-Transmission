# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:02:06 2020

@author: berei
"""
import time
import numpy as np
import cv2

img=cv2.imread('DrTong.jpg')
def a(img,qual):
    s=time.time()
    tmp = cv2.imencode('.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY), qual])
    print((time.time()-s)*1000)
    print(qual)
    return tmp

for i in range(90):
    qual=10+i
    a(img,qual)