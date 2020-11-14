#!/usr/bin/env python
# coding: utf-8

# In[3]:


class ImgD:               
    def img_det(self,img_path):
        try:
            import cv2
            import numpy as np
            label_path = "Essentials\\Yolo\\coco.names"
            config_path = "Essentials\\Yolo\\yolov3.cfg"
            weight_path = "Essentials\\Yolo\\yolov3.weights"
            network = cv2.dnn.readNetFromDarknet(config_path,weight_path)
            ln =  network.getUnconnectedOutLayersNames()
            label = open( label_path).read().split()
            yolo_shape = (416,416)
            img = cv2.imread(img_path)
            H,W = img.shape[:2]
            pre_img = cv2.dnn.blobFromImage(img,1/255.0,yolo_shape,swapRB=True)
            network.setInput(pre_img)
            layer_out = network.forward(ln)
            Box = []
            Confidance =[]
            Labels = []
            for output in layer_out:
                for acc in output:
                    class_id = np.argmax(acc[5:])
                    confidence = acc[5:][class_id]
                    if float(confidence)>.90:
                        CenterX,CenterY,Width,Height = (acc[:4]*np.array([W,H,W,H])).astype("int")
                        X,Y = int(CenterX - Width/2), int(CenterY - Height/2)
                        Box.append([X,Y,int(Width),int(Height)])
                        Confidance.append(float(confidence))
                        Labels.append( label[class_id])        
            best_output = cv2.dnn.NMSBoxes(Box,Confidance,.5,.4)
            for i in range(len(Box)):
                if i in best_output:
                    X,Y,W,H=Box[i]
                    cv2.rectangle(img,(X,Y),(X+W,Y+H),(0,255,0),2)
                    cv2.putText(img,Labels[i],(X,Y-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
            img = cv2.resize(img,(800,800))
            while True:
                cv2.imshow("Image Object Detection",img)
                if cv2.waitKey(1)==13:
                    break
            cv2.destroyAllWindows()
            return True
        except:
            return False
    def live_det(self):
        
        try:
            import cv2
            import numpy as np
            cam = cv2.VideoCapture(0)
            count =0
            def live_image(img):
                Box = []
                Confidance = []
                Labels = []
                label_path = "Essentials\\Yolo\\coco.names"
                config_path = "Essentials\\Yolo\\yolov3.cfg"
                weight_path = "Essentials\\Yolo\\yolov3.weights"
                network = cv2.dnn.readNetFromDarknet(config_path,weight_path)
                ln =  network.getUnconnectedOutLayersNames()
                label = open( label_path).read().split()
                yolo_shape = (416,416)
                H,W = img.shape[:2]
                pre_img = cv2.dnn.blobFromImage(img,1/255.0, yolo_shape,swapRB=True)
                network.setInput(pre_img)
                layers_out =  network.forward( ln)
                for output in layers_out:
                    for acc in output: 
                        class_id = np.argmax(acc[5:])
                        confidence = acc[5:][class_id]
                        if float(confidence)>.85: 
                            CenterX,CenterY,Width,Height = (acc[:4]*np.array([W,H,W,H])).astype("int")
                            X,Y = int(CenterX-Width/2),int(CenterY-Height/2)
                            Box.append([X,Y,int(Width),int(Height)])
                            Confidance.append(float(confidence))
                            Labels.append( label[class_id])
                best_out = cv2.dnn.NMSBoxes(Box,Confidance,.5,.4)
                for i in range(len(Box)):
                    if i in best_out:
                        X,Y,W,H = Box[i]
                        cv2.rectangle(img,(X,Y),(X+W,Y+H),(0,0,255),2)
                        cv2.putText(img,Labels[i],(X,Y-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
                return img
            while True:
                temp,img = cam.read()
                if temp:
                    img = live_image(img)
                    cv2.imshow("Live Camera Object Detection",img)
                    if cv2.waitKey(1)==13:
                        break
                else:
                    count+=1
                    if count==30:
                        return False
            cam.release()
            cv2.destroyAllWindows()
            return True
        except:
            return False
 

