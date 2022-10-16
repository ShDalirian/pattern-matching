import cv2
import numpy as np
from pattern_detection import *

min_similarity:float=0.8
pattern=255*np.ones((20,20,1),dtype=np.uint8)
for y in range(pattern.shape[0]):
    for x in range(pattern.shape[1]):
        if (y>pattern.shape[0]//4 and x>pattern.shape[1]//4) and (y<3*pattern.shape[0]//4 and x<3*pattern.shape[1]//4):
            pattern[y,x]=np.zeros((1,1),dtype=np.uint8)

img=255*np.ones((50,50,1),dtype=np.uint8)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if (y>pattern.shape[0]//4 and x>pattern.shape[1]//4) and (y<3*pattern.shape[0]//4 and x<3*pattern.shape[1]//4):
            img[y,x]=np.zeros((1,1),dtype=np.uint8)

pattern_area=pattern_similarity(img,pattern,min_similarity)
if pattern_area[2]<min_similarity:
    print("there is no pattern in image")
else:
    top_left_corner=(pattern_area[0],pattern_area[1])
    bottom_right_corner=(pattern_area[0]+pattern.shape[0],pattern_area[1]+pattern.shape[1])
    if img.shape[2]<2:
        BGR_image = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    BGR_image = cv2.rectangle(BGR_image,top_left_corner, bottom_right_corner, (0,0,255), 2)     
    cv2.imshow("pattern",BGR_image)
    cv2.waitKey(0)
