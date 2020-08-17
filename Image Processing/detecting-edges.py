# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:52:44 2020

@author: Teerth
Image Processing code
"""

import cv2

#loading the image
image = cv2.imread("C:/Users/Admin/Desktop/tomandjerry.jpg")
image2= cv2.imread("C:/Users/Admin/Desktop/me- cop - Copy.jpg")
#showing the image
#finding edges
edge = cv2.Canny(image, 0, 255)
edge2 = cv2.Canny(image2, 0, 255)
edge3 = cv2.Canny(image2, 150, 200)
#SHOWING THE IMAGE
cv2.imshow("edges", edge)
cv2.imshow("edge2", edge2)
cv2.imshow("asdf", edge3)
cv2.waitKey(0)


