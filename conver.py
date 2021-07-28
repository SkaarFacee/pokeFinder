
import cv2
import numpy as np
path="assets/img/1.png"
bg_path="bg.jpg"


# background = cv2.imread(path)
# foreground = cv2.imread(bg_path)

img1 = cv2.imread(path)
img2 = cv2.imread(bg_path)
r,c,v=img2.shape
img1=img1[:r,:c,:]
dst = cv2.addWeighted(img1, 0.5, img1, 0.7, 0)

img_arr = np.hstack((img1, img2))
cv2.imshow('Input Images',img_arr)
cv2.imshow('Blended Image',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()