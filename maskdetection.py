#!/usr/bin/env python
# coding: utf-8

# In[7]:


class md:
    def detection(self):
        import cv2
        import numpy as np
        from tensorflow.keras.preprocessing.image import img_to_array,load_img
        from tensorflow.keras.models import load_model
        from tensorflow.keras.applications.imagenet_utils import preprocess_input
        try:
            model = load_model("Essentials/Mask_Detection.h5")
            classifier = cv2.CascadeClassifier("Essentials/haarcascade_frontalface_default.xml")
            cam = cv2.VideoCapture(0)
            while True:
                temp,img = cam.read()
                if temp:
                    faces = classifier.detectMultiScale(img,1.3,3)
                    for x,y,w,h in faces:
                        image = img[y:y+h,x:w+x]
                        image = cv2.resize(image,(224,224))
                        image = img_to_array(image)
                        image = np.expand_dims(image,axis =0)
                        image = preprocess_input(image)

                        text = ""
                        color = (0,0,0)

                        pred = model.predict(image)[0]
                        if pred[0]>pred[1]:
                            text = "Mask Detected"
                            color = (0,255,0)
                        else:
                            text = "No Mask"
                            color = (0,0,255)
                        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                        cv2.putText(img,text,(x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)


                    cv2.imshow("Working",img)
                    if cv2.waitKey(1)==13:
                         break
            cam.release()
            cv2.destroyAllWindows()
            return True
        except:
            return False
                
        


# In[8]:




