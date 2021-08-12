# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:19:51 2021

@author: bhara
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    
    cv2.imshow('frame',frame)
   # if cv2.waitkey(20) & 0xFF == ord('q'):
        #break