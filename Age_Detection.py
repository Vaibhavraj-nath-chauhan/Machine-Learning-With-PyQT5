#!/usr/bin/env python
# coding: utf-8

# In[16]:


class ad:
    def age_det(self):
        try:
            import cv2
            cam = cv2.VideoCapture(0)
            classifier = cv2.CascadeClassifier("Essentials/haarcascade_frontalface_default.xml")
            MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

            ######   AGE
            deploy_age = "Essentials/Age Detection/deploy_age.prototxt"
            age_net = "Essentials/Age Detection/age_net.caffemodel"
            age_detection = cv2.dnn.readNetFromCaffe(deploy_age,age_net)
            age_list = ['(0)','(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']

            ######   Gender
            deploy_gender = "Essentials/Age Detection/deploy_gender.prototxt"
            gender_net = "Essentials/Age Detection/gender_net.caffemodel"
            gender_detection = cv2.dnn.readNetFromCaffe(deploy_gender,gender_net)
            gender_list = ['Male', 'Female']

            while True:
                temp,img = cam.read()
                if temp:
                    img = cv2.flip(img,1)
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = classifier.detectMultiScale(gray,1.2,5)
                    for (x,y,w,h) in faces:
                        face = img[y:y+h,x:x+w]
                        blob = cv2.dnn.blobFromImage(face,1,(244,244),MODEL_MEAN_VALUES,swapRB=True)

                        #Age
                        age_detection.setInput(blob)
                        pred = age_detection.forward()
                        age = age_list[pred[0].argmax()]

                        #Gender
                        gender_detection.setInput(blob)
                        pred = gender_detection.forward()
                        gender = gender_list[pred[0].argmax()]

                        overall = "{}, {}".format(age,gender)
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                        cv2.putText(img,overall,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.5,(98,255,255),1)

                        #predict Age
                    cv2.imshow("Age Detection",img)
                    if cv2.waitKey(1)==13:
                        break
            cam.release()
            cv2.destroyAllWindows()
            return True
        except:
            return False

