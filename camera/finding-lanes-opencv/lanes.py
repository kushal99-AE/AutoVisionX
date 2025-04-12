#import libararies
import cv2

#Read the image
image = cv2.imread('camera/finding-lanes-opencv/images/road-image-test.jpg')
#Display the image
cv2.imshow('result', image)

#Wait for a key press and close the image window
cv2.waitKey(0)