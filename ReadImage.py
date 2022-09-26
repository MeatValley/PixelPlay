# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import cv2

# Save image in set directory
# Read RGB image
img = cv2.imread('pedrin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Output img with window name as 'image'
cv2.imshow('image', img)
cv2.imshow('gray', gray)

thresh = 127
im_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
(thresh, im_bw_otsu) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('bin', im_bw)
cv2.imshow('bin_ostu', im_bw_otsu)

thresh = 200
im_bw_test = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('bin_test', im_bw_test)
thresh = 170
im_bw_test2 = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('bin_test2', im_bw_test2)



# Maintain output window utill
# user presses a key
cv2.waitKey(0)	

# Destroying present windows on screen
cv2.destroyAllWindows()
