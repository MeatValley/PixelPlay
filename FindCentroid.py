
# importing OpenCV(cv2) module
import cv2
import numpy as np

# Save image in set directory
# Read RGB image
img = cv2.imread('CepGray.jpg')

v = []
v2 = []


(h, w) = img.shape[:2]
# cv2.imshow("Original", image)
# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

line_center = 0
line_area = 0

# x,y starts from de left top corner
# x goes down, y goes right

for p in range(0,w):
    for j in range(0,h):
        if ( img[p, j][1] > 220):
            line_area = line_area+1
            line_center = line_center + j


    if(line_area == 0):
        line_center = cX
    else:
        line_center = line_center/line_area
        
    # img[p, int(line_center)-3: int(line_center)+3] = (0,255,0)
    v.append(line_center)

    line_area = 0
    line_center = 0
tx = 0

for x in v:
    tx = tx + x 

x_center = tx/557


column_area = 0
column_center = 0
for p in range(0,h):
    for j in range(0,w):
        if ( img[j, p][1] > 220):
            column_area = column_area+1
            column_center = column_center + j

    if(column_area == 0):
        column_center = cY
    else:
        column_center = column_center/column_area
        
    # img[p, int(column_center)-3: int(column_center)+3] = (0,0,255)
    v2.append(column_center)
    column_area = 0
    column_center = 0

ty=0
for y in v2:
    ty+=y
y_center = ty/557

print(x_center, y_center)
img_center = 0





img[int(x_center)-3:int(x_center)+3, int(y_center)-3:int(y_center)+3] = (255,0,255)
img[cX-3:cX+3, cY-3:cY+3] = (255,0,0)
cv2.imshow('geometric center', img)


# Maintain output window utill
# user presses a key
cv2.waitKey(0)	

# Destroying present windows on screen
cv2.destroyAllWindows()
