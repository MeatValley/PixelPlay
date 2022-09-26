# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2
import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="Monalisa.jpg", help="path to the input image")
args = vars(ap.parse_args())

# Save image in set directory
# Read RGB image
img = cv2.imread('Monalisa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
# cv2.imshow("Original", image)
# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)
print(h, w)


# Output img with window name as 'image'
(thresh, im_bw_otsu) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.imshow('bin_ostu', im_bw_otsu)

img[0:cX, 0:cY] = [0,255,0]
gray[0:1500, 0:300] = 0
cv2.imshow('update', img)
cv2.imshow('gray',gray )
dimensions = gray.shape
print(dimensions)


# Maintain output window utill
# user presses a key
cv2.waitKey(0)	

# Destroying present windows on screen
cv2.destroyAllWindows()
