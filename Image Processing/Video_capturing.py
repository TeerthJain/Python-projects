# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:58:24 2020

@author: Teerth 
Video Processing Course , Botlab
"""
import cv2
#import keyboard
#to access the camera we need a camera address which is here 0
#to capture a video

video =  cv2.VideoCapture(0)
while True:
    ret, is_caputuring = video.read()
    cv2.imshow("video", is_caputuring)
    #we have to remove the cv2.waitKey(1) to use the below if 
    #cv2.waitKey(1)//1 is necessary here
    #we can also use this method
    #if keyboard.is_pressed('q'):
     #   break
    if cv2.waitKey(1) == 113:#113 is the ascii code for q
        break
        
    
video.release()
cv2.destroyAllWindows()



