import cv2
import numpy as np

def array_equality(a,b,tol:int=10):
    ## Note1: two array should be in the same size
    equality:int=0
    if a.shape==b.shape:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                if a[i,j,:]>=b[i,j,:]*(1-tol/100) and a[i,j,:]<=b[i,j,:]*(1+tol/100):
                    equality +=1
    else:
        print("these arrays are not in the same size.")
    return equality/a.size


def pattern_similarity(in_img,pattern,min_similarity:float=0.8):
    #location=np.array([0,0],dtype=bool)
    x_step:int=pattern.shape[1]
    y_step:int=pattern.shape[0]

    # if necessary convert input image and pattern to gray scale to be unique
    if in_img.shape[2]>1:
        in_img=cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
    if pattern.shape[2]>1:
        pattern=cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)

    if x_step<=in_img.shape[1] and y_step<=in_img.shape[0]:     #check if pattern is smaller than the input image or not. if pattern is bigger just show an massage for it
        y:int=0
        x:int=0
        patterns_area=np.array([-1,-1,0],dtype=np.uint8)
        while y<in_img.shape[0]-y_step:
            while x<in_img.shape[1]-x_step:
                    similarity=array_equality(in_img[y:y+y_step,x:x+x_step],pattern)
                    if similarity>min_similarity:
                        print("this is similar to pattern\nthe probablity is equal to: "+str(similarity))
                        patterns_area[0:3]=[x,y,similarity] #np.vstack([patterns_area,[y,x,similarity]])
                        x +=x_step
                    else:
                        x +=1
            y +=1
    else:
        print("pattern is bigger than image\npattern match is not possible!")

    return patterns_area
