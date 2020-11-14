#!/usr/bin/env python
# coding: utf-8

# In[1]:


class cd:
    
    def car_live_de(self,vid_path):
        try :
            import cv2
            from time import sleep
            cam = cv2.VideoCapture(vid_path)
            classifier = cv2.CascadeClassifier("Essentials/cars.xml")
            def working(img):
                sleep(.06)
                img = cv2.resize(img,(600,600))
                cars = classifier.detectMultiScale(img,1.1,2)
                for (x,y,w,h) in cars:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Car",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.7,(0,0,255),1)
                return img
            while True:
                temp,img = cam.read()
                if temp:
                    img = working(img)
                    cv2.imshow("Live Car Detection",img)
                    if cv2.waitKey(1)==13:
                        break
                else:
                    return False
            cv2.destroyAllWindows()
            return True
        except:
            return False
    def car_img_de(self,img_path):
            import numpy as np
            import cv2
            label_path = "Essentials\\Yolo\\coco.names"
            config_path = "Essentials\\Yolo\\yolov3.cfg"
            weights_path = "Essentials\\Yolo\\yolov3.weights"
            yolo_shape = (416,416)
            network = cv2.dnn.readNetFromDarknet(config_path,weights_path)
            ln = network.getUnconnectedOutLayersNames()
            label = open(label_path).read().split()

            def car_detection(img):
                img = cv2.resize(img,(800,800))
                H,W = img.shape[:2]
                pre_image = cv2.dnn.blobFromImage(img,1/255.0,yolo_shape,swapRB=True)
                network.setInput(pre_image)
                layers_out = network.forward(ln)
                Box =[]
                Confidance =[]
                Label =[]
                for out in layers_out:
                    for acc in out:
                        class_id = np.argmax(acc[5:])
                        confidance = acc[5:][class_id]
                        if float(confidance)>.85:
                            if label[class_id] in ["car","moterbike","bus","truck"]: 
                                CenterX,CenterY,Width,Height = (acc[:4]*np.array([W,H,W,H])).astype("int")
                                X,Y = int(CenterX-Width/2),int(CenterY-Height/2)
                                Box.append([X,Y,int(Width),int(Height)])
                                Confidance.append(float(confidance))
                                Label.append(label[class_id])
                best_out = cv2.dnn.NMSBoxes(Box,Confidance,.5,.4)
                for i in range(len(Box)):
                    if i in best_out:
                        X,Y,W,H = Box[i]
                        cv2.rectangle(img,(X,Y),(X+W,Y+H),(0,255,0),2)
                        cv2.putText(img,Label[i],(X,Y-5),cv2.FONT_HERSHEY_COMPLEX,.6,(0,0,255),1)      
                return img
            img = cv2.imread(img_path)
            img = car_detection(img)
            while True:
                    cv2.imshow("Image Car Detection",img)
                    if cv2.waitKey(1)==13:
                        break
            cv2.destroyAllWindows()
            return True

