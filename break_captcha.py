# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:30:04 2020

@author: Shikhar
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image


def get_string(img):
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    #noise removal
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    
    #used pytesseract
    result = pytesseract.image_to_string(img)

    print(result)
    return result



import os
directory = r'C:\Users\hp\Desktop\solving_captchas_code_examples\generated_captcha_images'


for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image=cv2.imread(filename)
        result=get_string(image)
        cv2.imshow(result,  image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
