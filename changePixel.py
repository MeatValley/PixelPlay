# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2
import matplotlib.pyplot as plt


# Save image in set directory
# Read RGB image
img = cv2.imread('LorenaDurmindo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = img
(h, w) = image.shape[:2]
# cv2.imshow("Original", image)
# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

# Output img with window name as 'image'
(thresh, im_bw_otsu) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
dim = (1000,600)
# cv2.imshow('bin_ostu', im_bw_otsu)
invert = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# img[0:cX, 0:cY] = [255,255,255] - img[0:cX, 0:cY]
invert [0:1500, 0:900] = [255,255,255] - invert [0:1500, 0:900]
cv2.imshow('update', invert)

dimensions = gray.shape
print(dimensions)


# Maintain output window utill
# user presses a key
cv2.waitKey(0)	

# Destroying present windows on screen
cv2.destroyAllWindows()
