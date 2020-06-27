# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:17:42 2020

@author: xq141
"""

import cv2
import numpy as np
original=cv2.imread("test2.JPG",1)
blue,green,red=cv2.split(original)
mask=np.full(blue.shape,255,dtype=np.uint8)
#gray = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
equal=cv2.equalizeHist(blue)
cv2.imwrite('equalizeHist.jpg',equal)
#cancerCell=cv2.bilateralFilter(cancerCell,25,100,100)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
k=np.ones((9,9),np.uint8)
e=cv2.erode(equal,k,iterations=1)
b=cv2.subtract(equal,e)
cv2.imwrite('eroSubtract.jpg',b)
t,cancerCell=cv2.threshold(b,10,255,cv2.THRESH_BINARY)
cv2.imwrite('threshold.jpg',cancerCell)
close=cv2.morphologyEx(cancerCell,cv2.MORPH_CLOSE,kernel,iterations=3)
cv2.imwrite('morphologyExClose.jpg',close)
img = cv2.cvtColor(close,cv2.COLOR_GRAY2BGR)
result=cv2.addWeighted(img,1,original,1,0)
removeFromOriginal=cv2.bitwise_xor(close,mask)
removeFromOriginal = cv2.cvtColor(removeFromOriginal,cv2.COLOR_GRAY2BGR)
removeFromOriginal=cv2.bitwise_or(original,removeFromOriginal)
cv2.imwrite('removeFromOriginal.jpg',removeFromOriginal)
cv2.imwrite('whiteBackground.jpg',result) 