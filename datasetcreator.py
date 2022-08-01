import numpy as np
import cv2 
import time
prev=time.time()
cnt=118
camera= cv2.VideoCapture(0)
i=0
area=0
print('Please Enter you name:(numberonly) ')
nam=input()
while(1):
    success,frame = camera.read()
    b = cv2.GaussianBlur(frame, (0,0), sigmaX=9, sigmaY=9)
    hsv=cv2.cvtColor(b,cv2.COLOR_BGR2HSV)
    
    lower_limit=(63,0,0)
    upper_limit=(179,212,132)
    only_green=cv2.inRange(hsv,lower_limit,upper_limit)
    
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(only_green, kernel, iterations=1)
    # img_erosion = cv2.dilate(img_erosion, kernel, iterations=1)
    cv2.imshow('frame', img_erosion)
    height, width= img_erosion.shape
    # min_x, min_y = width, height
    # max_x = max_y = 0  
   
    cnts,hearachy= cv2.findContours(img_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, cnts, 0, (0, 255,0), 2)
    for contour in cnts:
        (x,y,w,h) = cv2.boundingRect(contour)
        area=(w+22)*(h+22) 
        if area>7000 and area < 20000:
            cv2.rectangle(frame, (x-22, y-22), (x+w+22, y+h+22), (255, 0, 0), 2)
            now=time.time()
            if now-prev>= 0.5 and y-20<y+h+20 and x-20<x+w+20 and  y-20>0 and x-20>0:
                prev=now
                print(area)
                cv2.imwrite('dataset/'+nam+'.'+str(cnt)+'.jpg',frame[y-20:y+h+20,x-20:x+w+20])
                cnt+=1
        # min_x, max_x = min(x, min_x), max(x+w, max_x)
        # min_y, max_y = min(y, min_y), max(y+h, max_y)
        # if w > 80 and h > 80:
        #     cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
        #     print('area  is ',w*h

        # if max_x - min_x > 0 and max_y - min_y > 0:
        #     area=(max_x-min_x+40)*(max_y-min_y+40)
        # if area>3000 and area < 20000:
        #     cv2.rectangle(frame, (min_x-22, min_y-22), (max_x+22, max_y+22), (255, 0, 0), 2)
        #     now=time.time()
        #     if now-prev>= 1:
        #         prev=now
        #         cnt+=1
                    # cv2.imwrite('dataset/'+nam+'.'+str(cnt)+'.jpg',frame[min_y-20:max_y+20,min_x-20:max_x+20])
                    # print(prev)
    # for contour in cnts:
  
    #     # here we are ignoring first counter because 
    #     # findcontour function detects whole image as shape
    #     if i == 0:
    #         i = 1
    #         continue
    #     area = cv2.contourArea(contour)
    #     if area>700:
    #         # cv2.approxPloyDP() function to approximate the shape 
    #         approx = cv2.approxPolyDP(
    #             contour, 0.01 * cv2.arcLength(contour, True), True)
    #         # using drawContours() function
    #         cv2.drawContours(frame, [approx], 0, (0, 255,0), 2)   
            
         

    
        

    cv2.imshow('shapes', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'): #converts the binary key press value to decimal which is 113
        break