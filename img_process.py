
import json
import cv2
import numpy as np
import os 

def read_img(path1,path2):
    return cv2.imread(path1,-1),cv2.imread(path2,-1)

def preprocess(img,size):
    img[img<30]=255
    return cv2.resize(img,size,cv2.INTER_AREA)

def bg_shape(img):
    return cv2.resize(img,(1280,554),interpolation=cv2.INTER_CUBIC)

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
    _,masker=cv2.threshold(img,230,255,cv2.THRESH_BINARY)
    return masker 

def cycle(path1,path2):
    img1,img2=read_img(path1=path1,path2=path2)
    img1=preprocess(img1,(350,350))
    img2=bg_shape(img2[:,:,:3])
    img1_grey=get_grayscale(img1)
    x1,x2,y1,y2=center(img1,img2)
    roi=get_roi(img2,x1,x2,y1,y2)
    mask=get_mask(img1_grey)
    com_bg=cv2.bitwise_or(roi,roi,mask=mask)
    mask_inv = cv2.bitwise_not(img1_grey)
    fg = cv2.bitwise_and(img1,img1, mask=mask_inv)
    final_roi = cv2.addWeighted(com_bg,1,fg[:,:,:3],1,0)
    img2[x1:x2,y1:y2]=final_roi
    # cv2.imshow("RESULT",img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img2

if __name__ == '__main__':
    bgs=[x.split('.')[0] for x in os.listdir('assets/backgrounds/')]
    base_path="assets/img/"
    base_bg="assets/backgrounds/"
    with open('assets/legend/legend.json') as file:
        data = json.load(file) 
    for bg_name in bgs:
        for save_name,name in data.items():
            path1=base_path+save_name+".png"
            path2=base_bg+bg_name+'.jpg'
            img=cycle(path1,path2)
            cv2.imwrite("assets/dataset/"+str(bg_name)+"_"+str(save_name)+".jpg",img)
    