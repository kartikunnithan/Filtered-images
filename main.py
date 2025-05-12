import cv2
import numpy as np
def apply_filter(image,key):
    filtered=image.copy()
    if key ==ord('r'): 
        filtered[:,:,0]=0
        filtered[:,:,1]=0
    elif key==ord('g'):
        filtered[:,:,0]=0
        filtered[:,:,2]=0
    elif key==ord('b'):
        filtered[:,:,1]=0
        filtered[:,:,2]=0
    elif key==ord('1'):
        filtered[:,:,2]=cv2.add(filtered[:,:,2], 50)
    elif key==ord('2'):
        filtered[:,:,0]=cv2.subtract(filtered[:,:,0], 50)
    return filtered
image=cv2.imread('image.png')
if image is None: 
    print("Error:Image not found")
    exit()
cv2.imshow('Filtered Image', image)
while True:
    key=cv2.waitKey(0)
    if key == ord('q'):
        break
    image_filtered=apply_filter(image,key)
    cv2.imshow('Filtered Image', image_filtered)
cv2.destroyAllWindows()

