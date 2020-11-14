#!/usr/bin/env python
# coding: utf-8

# In[397]:


class sd:
    def sosi_di(self,img_path):
        try:
            import cv2
            import numpy as np
            label_path = "Essentials\\Yolo\\coco.names"
            config_path = "Essentials\\Yolo\\yolov3.cfg"
            weight_path = "Essentials\\Yolo\\yolov3.weights"
            network = cv2.dnn.readNetFromDarknet(config_path,weight_path)
            ln =  network.getUnconnectedOutLayersNames()
            label = open(label_path).read().split()
            yolo_shape = (416,416)
            img = cv2.imread(img_path)
            img = cv2.resize(img,yolo_shape)
            H,W = img.shape[:2]
            pre_img = cv2.dnn.blobFromImage(img,1/255.0,yolo_shape,swapRB=True)
            network.setInput(pre_img)
            layers = network.forward(ln)
            Box = []
            Confidance =[]
            Centers = []
            for out in layers:
                for acc in out:
                    score = acc[5:]
                    class_id = np.argmax(score)
                    confidance = score[class_id]
                    if float(confidance)>.85:
                        Object = label[class_id]
                        if Object =="person":
                            CenterX,CenterY,Width,Height = (acc[:4]*np.array([W,H,W,H])).astype("int")
                            X,Y = int(CenterX-Width/2), int(CenterY-Height/2)
                            Box.append([X,Y,int(Width),int(Height)])
                            Confidance.append(float(confidance))
                            Centers.append([CenterX,CenterY])
            best_out = cv2.dnn.NMSBoxes(Box,Confidance,0.5,0.4)
            for i in range(len(Box)):
                if i in best_out:
                    x,y,w,h = Box[i]
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            d = []
            for i in range(len(Box)):
                if i in best_out:
                    for j in range(i+1,len(Box)):
                        if j in best_out:
                            X,Y,W,H = Box[i]
                            x,y,w,h = Box[j]
                            distance = np.sqrt((Centers[i][0]-Centers[j][0])**2+(Centers[j][0]-Centers[j][1])**2)
                            d.append(distance)
                            if distance < 90:
                                cv2.rectangle(img,(X,Y),(X+W,Y+H),(0,0,255),2)
                                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

            while True:
                cv2.imshow("Social Distancing",img)
                if cv2.waitKey(1)==13:
                    break
            cv2.destroyAllWindows()
            return d
        except:
            return False

