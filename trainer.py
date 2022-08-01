import cv2
import os
import numpy as np
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_samples=[]
Ids=[]
dir_list = os.listdir('dataset/')
for data in dir_list:
    image=cv2.imread('dataset/'+data,0)
    face_samples.append(image)
    idnam=data.split('.')
    Ids.append(int(idnam[0]))
    # print(Ids)
recognizer.train(face_samples,np.array(Ids))
print('training')
recognizer.save('trainningData.xml')
