# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:47:28 2020

@author: Admin
"""
import cv2
face_algo = cv2.CascadeClassifier("C:/Users/Admin/Desktop/Image Processing/pics/haarcascade_frontalface_alt.xml")
video = cv2.VideoCapture(0)
while True:
    ret, is_capturing = video.read()
    gray_scale = cv2.cvtColor(is_capturing, cv2.COLOR_BGR2GRAY)
    face_detection = face_algo.detectMultiScale(gray_scale)
    #below the _str stands for starting point 
    #and _end stands for end point
    for (w_str, h_str, w_end, h_end) in face_detection:
        cv2.rectangle(is_capturing, (w_str, h_str), (w_str + w_end, h_str + h_end), (0, 0, 255), 2)
        
    cv2.imshow("face-detection", is_capturing)
    if cv2.waitKey(1) == 113:
        break
   
video.release()
cv2.destroyAllWindows()