# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:19:11 2020

@author: Teerth
Image processing course, Botlab
"""

import cv2

#loading the image
image = cv2.imread("C:/Users/Admin/Desktop/tomandjerry.jpg")
image2= cv2.imread("C:/Users/Admin/Desktop/me- cop - Copy.jpg")
#creating the rectangle
#(image_File, (starting point, point2(from the border)), (ending point, point2(from the middle))
#, (color gbr format), thickness
cv2.rectangle(image2, (100, 7),(300, 200), (0, 255, 255), 4) 
#showing the image
cv2.imshow("me", image2)
cv2.waitKey(0)

