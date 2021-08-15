
from os import name
import cv2
import numpy as np



def read_img(path1,path2):
    return cv2.imread(path1,-1),cv2.imread(path2,-1)

def resize(img,size):
    return cv2.resize(img,size,cv2.INTER_AREA)

def remove_blacks(img):
    img[img<30]=255
    return img

def get_grayscale(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def center(img1,img2):
    bg_center_x=img2.shape[0]/2
    bg_center_y=img2.shape[1]/2
    new_x_start=int(bg_center_x-(img1.shape[0]/2))
    new_x_end=int(bg_center_x+(img1.shape[0]/2))
    new_y_start=int(bg_center_y-(img1.shape[1]/2))
    new_y_end=int(bg_center_y+(img1.shape[1]/2))
    
    return new_x_start,new_x_end,new_y_start,new_y_end

def get_roi(img,x1,x2,y1,y2):
    return img[x1:x2,y1:y2]

def get_mask(img):
    _,masker=cv2.threshold(img1_grey,130,255,cv2.THRESH_BINARY)
    return masker 

if __name__ == '__main__':
    path="assets/img/1.png"
    bg="assets/backgrounds/arena.jpg"
    img1,img2=read_img(path1=path,path2=bg)
    img1=resize(img1,(350,350))
    img1=remove_blacks(img1)
    img1_grey=get_grayscale(img1)
    
    
    x1,x2,y1,y2=center(img1,img2)
    roi=get_roi(img2,x1,x2,y1,y2)
    mask=get_mask(img1_grey)
    com_bg=cv2.bitwise_or(roi,roi,mask=mask)
    mask_inv = cv2.bitwise_not(img1_grey)
    fg = cv2.bitwise_and(img1,img1, mask=mask_inv)
    final_roi = cv2.addWeighted(com_bg,0.4,fg[:,:,:3],1,0)

    cv2.imshow("RESULT",final_roi)
    cv2.imshow("final mask",fg[:,:,:3])  
    cv2.imshow("image",img1)
    cv2.imshow("grey img",img1_grey)
    cv2.imshow("mask", mask) #show mask
    cv2.imshow("tada",com_bg)
    cv2.imshow("mask inv",mask_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()