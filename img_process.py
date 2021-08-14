
import cv2
import numpy as np
path="assets/img/1.png"
bg="assets/backgrounds/arena.jpg"
pokemon = cv2.imread(path)
backgroud=cv2.imread(bg,-1)



bg_center_x=backgroud.shape[0]/2
bg_center_y=backgroud.shape[1]/2

roi=backgroud[int(bg_center_x-(pokemon.shape[0]/2)):int(bg_center_x+(pokemon.shape[0]/2)),int(bg_center_y-(pokemon.shape[1]/2)):int(bg_center_y+(pokemon.shape[1]/2))]

masker=cv2.threshold(pokemon,30,255,cv2.THRESH_BINARY)
cv2.imshow("pokemon",cv2.resize(pokemon,(200,200),interpolation=cv2.INTER_AREA))
cv2.imshow("bg",roi)

fin=cv2.addWeighted(pokemon,0.5,roi,0.5,0)
# cv2.imshow("test",masker)
print(masker)
cv2.imshow("f",masker)

cv2.waitKey(0)
cv2.destroyAllWindows()