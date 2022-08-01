#import opencv and numpy
import cv2
from cv2 import imread  
import numpy as np

#trackbar callback fucntion to update HSV value
def callback(x):
	global H_low,H_high,S_low,S_high,V_low,V_high
	#assign trackbar position value to H,S,V High and low variable
	H_low = cv2.getTrackbarPos('low H','controls')
	H_high = cv2.getTrackbarPos('high H','controls')
	S_low = cv2.getTrackbarPos('low S','controls')
	S_high = cv2.getTrackbarPos('high S','controls')
	V_low = cv2.getTrackbarPos('low V','controls')
	V_high = cv2.getTrackbarPos('high V','controls')


#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);


#global variable
H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

#create trackbars for high,low H,S,V 
cv2.createTrackbar('low H','controls',0,179,callback)
cv2.createTrackbar('high H','controls',179,179,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)

camera= cv2.VideoCapture(0)

while(1):
	success,b=camera.read()
	frame = cv2.GaussianBlur(b, (0,0), sigmaX=9, sigmaY=9)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv_low = np.array([H_low, S_low, V_low], np.uint8)
	hsv_high = np.array([H_high, S_high, V_high], np.uint8)
	mask = cv2.inRange(hsv, hsv_low, hsv_high)
	# print (mask)
	res = cv2.bitwise_and(frame, frame, mask=mask)



	#show image
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	#waitfor the user to press escape and break the while loop
	k = cv2.waitKey(10) & 0xFF
	if k == 113:
		break
		
#destroys all windo
cv2.destroyAllWindows()