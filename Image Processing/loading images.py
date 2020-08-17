# -*- coding: utf-8 -*-
"""
Created by Teerth Jain on 28/4/2020

Image processing course(BotLab)

"""

import cv2



image = cv2.imread("C:/Users/Admin/Desktop/tomandjerry.jpg")
image2= cv2.imread("C:/Users/Admin/Desktop/me- cop - Copy.jpg")
cv2.imshow('image', image)
cv2.imshow('image2', image2)

cv2.waitKey(0) 