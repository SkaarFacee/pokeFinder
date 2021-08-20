import cv2
import pandas as pd
import json 
bgs=["arena","canyon","cave","city","coast","detective","forest","glacier","gym","volcano"]
base_path="assets/dataset/"
with open('assets/legend/legend.json') as file:
    data = json.load(file) 
for bg in bgs:
    for num,name in data.items():
        img=cv2.imread(base_path+bg+"_"+str(num)+str(".jpg"))
        f=pd.Series(data=img)
        break
    break
print(f)
cv2.imshow("temp.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()