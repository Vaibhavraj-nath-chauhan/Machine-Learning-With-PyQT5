#!/usr/bin/env python
# coding: utf-8

# In[6]:


class registration:
    def register_function(self):
        import cv2
        cassifier = cv2.CascadeClassifier("Essentials/haarcascade_frontalface_default.xml")
        cam = cv2.VideoCapture(0)
        count =0
        while True:
            _,img = cam.read()
            if _:
                gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = cassifier.detectMultiScale(gray_img,1.3,6) 
                for x,y,w,h in faces:
                    count+=1
                    face = gray_img[y:y+h,x:x+w]
                    face = cv2.resize(face,(200,200))
                    cv2.imwrite("Images\\sample{}.jpg".format(count),face)
                if count==50:
                    break
                if cv2.waitKey(1) == 13:
                    break
        cam.release()
        cv2.destroyAllWindows()
    
    def login_function(self):
        import os 
        import cv2
        import numpy as np
        train =[]
        try:
            if len(os.listdir("Images/"))>=5:
                labels = np.arange(1,len(os.listdir("Images/")))
                labels = np.asarray(labels,dtype = np.int32)
                for i in os.listdir("Images/"):
                    if i[-4:]==".jpg":
                        img = cv2.imread("Images/"+i,cv2.IMREAD_GRAYSCALE)
                        img = np.asarray(img,dtype = np.uint8)
                        train.append(img)
            face_model = cv2.face_LBPHFaceRecognizer.create()
            face_model.train(train,labels)
            cassifier = cv2.CascadeClassifier("Essentials/haarcascade_frontalface_default.xml")
            cam = cv2.VideoCapture(0)
            pred_lis = []
            count=0
            while True:
                _,img = cam.read()
                if _:
                    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = cassifier.detectMultiScale(gray_img,1.3,6)
                    count+=1
                    for x,y,w,h in faces:
                        face = gray_img[y:y+h,x:x+w]
                        pred = face_model.predict(face)
                        if pred[1]<42:
                            cv2.putText(img,"Confirm",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,0),2)
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                            cam.release()
                            cv2.destroyAllWindows()
                            return 1
                        else:
                            cv2.putText(img,"Unknown",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,.5,(0,0,255),2)
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.imshow("work",img)
                    if count==200:
                        cam.release()
                        cv2.destroyAllWindows()
                        return 0
                    if cv2.waitKey(1) == 13:
                         break
        except:
            return 0
        cam.release()
        cv2.destroyAllWindows()

