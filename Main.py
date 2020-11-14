#!/usr/bin/env python
# coding: utf-8

# # <center>Multiple Projects</center>

# <ol><li>PyQt5</li></ol>

# In[1]:


import PyQt5 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os 
import playsound
from gtts import gTTS
from playsound import playsound

list_up = os.listdir()
if "Images" not in list_up:
    os.mkdir("Images")

count= 0
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'My Project'
        self.left = 700
        self.top = 200
        self.width = 700
        self.height = 500
        self.statusBar().showMessage("Welcome")
        self.statusBar().setObjectName("bar")
        self.setFixedSize(self.height,self.width)
        with open("Css/Ml.css","r") as css:
            styleSheet = css.read()
        self.setStyleSheet(styleSheet)
        self.setObjectName("windows")
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #login Window.....................................................................................................
        if len(os.listdir("Images/")) <=10:
            self.login_window = QFrame(self)
            self.login_window.setObjectName("frame_1")
            self.login_window.move(55,100)
            self.login_window.setVisible(True)############################
            
            global count
            count =1
            
            self.login_window_text = QLabel(self.login_window)
            self.login_window_text.setObjectName("heading")
            self.login_window_text.setText("Registration")
            self.login_window_text.move(135,30)
            self.statusBar().showMessage("Face Sample")
            
            self.name = QLabel(self.login_window)
            self.name.setObjectName("text")
            self.name.setText("Name")
            self.name.move(30,130)
            
            self.name_q = QLineEdit(self.login_window)
            self.name_q.setObjectName("line_edit")
            self.name_q.setText("Enter Your Name")
            self.name_q.move(30,160)
    
            self.text_q = QLabel(self.login_window)
            self.text_q.setObjectName("text")
            self.text_q.setText("\tWelcome to our program\n\nWe need your face sample\n\n1. Allow Camera To Capture\n\n2. Have Some Patience Machine will take time")
            self.text_q.move(30,250)
            
            
            self.login_window_button_2 = QPushButton(self.login_window)
            self.login_window_button_2.setObjectName("login_B")
            self.login_window_button_2.setText("Face Recogination")
            self.login_window_button_2.move(145,420)
            self.login_window_button_2.clicked.connect(self.register)
        
        #login Window.........................
        self.login_window1 = QFrame(self)
        self.login_window1.setObjectName("frame_1")
        self.login_window1.move(55,100)
        if count ==0:
            self.login_window1.setVisible(True)#################################################################
        else:
            self.login_window1.setVisible(False)
            
            
        self.login_window_text1 = QLabel(self.login_window1)
        self.login_window_text1.setObjectName("heading")
        self.login_window_text1.setText("Login")
        self.login_window_text1.move(155,30)
        
            
        self.name1 = QLabel(self.login_window1)
        self.name1.setObjectName("text")
        self.name1.setText("Name")
        self.name1.move(30,80)
            
        self.name_q1 = QLineEdit(self.login_window1)
        self.name_q1.setObjectName("line_edit")
        self.name_q1.setText("Enter Your Name")
        self.name_q1.move(30,110)
            
        self.text_q1 = QLabel(self.login_window1)
        self.text_q1.setObjectName("text")
        self.text_q1.setText("\tWelcome to our program\n\nWe have your face sample\n\n1. Allow Camera\n\n2. Have Some Patience Machine will take time")
        self.text_q1.move(30,200)


        self.login_window_button1 = QPushButton(self.login_window1)
        self.login_window_button1.setObjectName("login_B")
        self.login_window_button1.setText("Login")
        self.login_window_button1.move(145,350)
        self.login_window_button1.clicked.connect(self.login)
            
            
        self.delete = QLabel(self.login_window1)
        self.delete.setObjectName("text")
        self.delete.setText("Delete Your Account")
        self.delete.move(30,420)
            
        self.delete_b = QPushButton(self.login_window1)
        self.delete_b.setObjectName("login_B")
        self.delete_b.setText("Delete")
        self.delete_b.move(30,450)
        self.delete_b.clicked.connect(self.delete_all)
        
        #first Window.....................................................................................................
        self.first_frame = QFrame(self)
        self.first_frame.setObjectName("frame_1")
        self.first_frame.move(55,100)
        self.first_frame.setVisible(False)
        
        #text part
        self.text_1 = QLabel(self.first_frame)
        self.text_1.setText("Services")
        self.text_1.setObjectName("heading")
        self.text_1.move(165,30)
        
#part 1...................................................................................
        self.button_1 = QPushButton(self.first_frame)
        self.button_1.setObjectName("button_1")
        self.button_1.setText("  Mask Detection  ")
        self.button_1.move(50,100)
        self.button_1.clicked.connect(self.mask)
        
        #second Window:---------
        
        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.move(100,100)
        self.frame_2.setVisible(False)    
        
        self.frame_2_head = QLabel(self.frame_2)
        self.frame_2_head.setObjectName("heading")
        self.frame_2_head.setText("Mask Detection")
        self.frame_2_head.move(80,30)
        
        self.frame_2_text = QLabel(self.frame_2)
        self.frame_2_text.setObjectName("text")
        self.frame_2_text.setText("\n\nClick on start to activate\nmask detection function\nand give permission to \nuse system camera\n\n\nPress Enter To Exit \nPopUp Camera")
        self.frame_2_text.move(50,100)
        
        self.frame_2_button = QPushButton(self.frame_2)
        self.frame_2_button.setObjectName("login_B")
        self.frame_2_button.setText("Start")
        self.frame_2_button.move(100,340)
        self.frame_2_button.clicked.connect(self.mask_detection)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_2)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
#part 2...................................................................................
        self.button_2 = QPushButton(self.first_frame)
        self.button_2.setObjectName("button_1")
        self.button_2.setText(" Face Classifier")                  
        self.button_2.move(250,100)
        self.button_2.clicked.connect(self.face)
        
        #third frame
        self.frame_3 = QFrame(self)
        self.frame_3.setObjectName("frame_2")
        self.frame_3.move(100,100)
        self.frame_3.setVisible(False)
        
        self.frame_3_head = QLabel(self.frame_3)
        self.frame_3_head.setObjectName("heading")
        self.frame_3_head.setText("Face Classifier")
        self.frame_3_head.move(80,30)
        
        self.frame_3_text = QLabel(self.frame_3)
        self.frame_3_text.setObjectName("text")
        self.frame_3_text.setText("\n\nClick on start to activate\nface Classifier function\nand give permission to \nuse system camera\n\n\nPress Enter To Exit \nPopUp Camera")
        self.frame_3_text.move(50,100)
        
        self.frame_3_button = QPushButton(self.frame_3)
        self.frame_3_button.setObjectName("login_B")
        self.frame_3_button.setText("Start")
        self.frame_3_button.move(100,340)
        self.frame_3_button.clicked.connect(self.face_classifier)
        #button function to add.............................
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_3)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
        
#part 3...................................................................................
        self.button_3 = QPushButton(self.first_frame)
        self.button_3.setObjectName("button_1")
        self.button_3.setText(" Object Detection 1")        
        self.button_3.move(50,200)
        self.button_3.clicked.connect(self.img_obj)
        
        #fourth frame
        self.frame_4 = QFrame(self)
        self.frame_4.setObjectName("frame_2")
        self.frame_4.move(100,100)
        
        self.frame_4.setVisible(False)
        
        self.frame_4_head = QLabel(self.frame_4)
        self.frame_4_head.setObjectName("heading")
        self.frame_4_head.setText("Image Object Detection")
        self.frame_4_head.move(50,50)
        
        self.frame_4_text = QLabel(self.frame_4)
        self.frame_4_text.setObjectName("text")
        self.frame_4_text.setText("\n\nClick on start to activate\nObject Detection function\n\n\nPress Enter To Exit \nPopUp Window")
        self.frame_4_text.move(50,100)
        
        self.frame_4_box = QLineEdit(self.frame_4)
        self.frame_4_box.setObjectName("line_edit")
        self.frame_4_box.setText("Select Image Location")
        self.frame_4_box.move(30,280)
        
        self.frame_4_button_dir = QPushButton(self.frame_4)
        self.frame_4_button_dir.setObjectName("but")
        self.frame_4_button_dir.setText("Select")
        self.frame_4_button_dir.move(200,280)
        self.frame_4_button_dir.clicked.connect(self.img_select)
        
        
        self.frame_4_button = QPushButton(self.frame_4)
        self.frame_4_button.setObjectName("login_B")
        self.frame_4_button.setText("Start")
        self.frame_4_button.move(100,340)
        self.frame_4_button.clicked.connect(self.img_class)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_4)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
#part 4...................................................................................
        self.button_4 = QPushButton(self.first_frame)
        self.button_4.setObjectName("button_1")
        self.button_4.setText(" Object Detection 2 ")      
        self.button_4.move(250,200)
        self.button_4.clicked.connect(self.live_obj)
        
        #fifth frame
        self.frame_5 = QFrame(self)
        self.frame_5.setObjectName("frame_2")
        self.frame_5.move(100,100)
        self.frame_5.setVisible(False)
        
        self.frame_5_head = QLabel(self.frame_5)
        self.frame_5_head.setObjectName("heading")
        self.frame_5_head.setText("Live Object Detection")
        self.frame_5_head.move(50,50)
        
        self.frame_5_text = QLabel(self.frame_5)
        self.frame_5_text.setObjectName("text")
        self.frame_5_text.setText("\n\nClick on start to activate\nObject Detection function\nand give permission to \nuse system camera\n\n\nPress Enter To Exit \nPopUp Camera")
        self.frame_5_text.move(50,100)
        
        self.frame_5_button = QPushButton(self.frame_5)
        self.frame_5_button.setObjectName("login_B")
        self.frame_5_button.setText("Start")
        self.frame_5_button.move(100,340)
        self.frame_5_button.clicked.connect(self.liv_det)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_5)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
        

#part 5...................................................................................
        self.button_5 = QPushButton(self.first_frame)
        self.button_5.setObjectName("button_1")
        self.button_5.setText("Social Distancing ")
        self.button_5.move(50,300)
        self.button_5.clicked.connect(self.social)
        
        #sixth frame frame
        self.frame_6 = QFrame(self)
        self.frame_6.setObjectName("frame_2")
        self.frame_6.move(100,100)
        self.frame_6.setVisible(False)
        
        self.frame_6_head = QLabel(self.frame_6)
        self.frame_6_head.setObjectName("heading")
        self.frame_6_head.setText("Social Distancing")
        self.frame_6_head.move(70,30)
        
        self.frame_6_text = QLabel(self.frame_6)
        self.frame_6_text.setObjectName("text")
        self.frame_6_text.setText("\n\nClick on start to activate\nSocial Distanceing function\n\n\nPress Enter To Exit \nPopUp Camera")
        self.frame_6_text.move(50,100)
        
        self.frame_6_box = QLineEdit(self.frame_6)
        self.frame_6_box.setObjectName("line_edit")
        self.frame_6_box.setText("Select Image Location")
        self.frame_6_box.move(30,280)
        
        self.frame_6_button_dir = QPushButton(self.frame_6)
        self.frame_6_button_dir.setObjectName("but")
        self.frame_6_button_dir.setText("Select")
        self.frame_6_button_dir.move(200,280)
        self.frame_6_button_dir.clicked.connect(self.img_select)
        
        self.frame_6_button = QPushButton(self.frame_6)
        self.frame_6_button.setObjectName("login_B")
        self.frame_6_button.setText("Start")
        self.frame_6_button.move(100,340)
        self.frame_6_button.clicked.connect(self.social_distance)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_6)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        

#part 6...................................................................................
        self.button_6 = QPushButton(self.first_frame)
        self.button_6.setObjectName("button_1")
        self.button_6.setText("  Car Detection 1 ")
        self.button_6.move(250,300)
        self.button_6.clicked.connect(self.car_img)
        
        
        #seventh frame frame
        self.frame_7 = QFrame(self)
        self.frame_7.setObjectName("frame_2")
        self.frame_7.move(100,100)
        self.frame_7.setVisible(False)
        
        self.frame_7_head = QLabel(self.frame_7)
        self.frame_7_head.setObjectName("heading")
        self.frame_7_head.setText("Image Car Detection")             
        self.frame_7_head.move(70,30)
        
        self.frame_7_text = QLabel(self.frame_7)
        self.frame_7_text.setObjectName("text")
        self.frame_7_text.setText("\n\nClick on start to activate\nCar Detection function\n\n\nPress Enter To Exit \nPopUp Camera")
        self.frame_7_text.move(50,100)
        
        self.frame_7_box = QLineEdit(self.frame_7)
        self.frame_7_box.setObjectName("line_edit")
        self.frame_7_box.setText("Select Image Location")
        self.frame_7_box.move(30,280)
        
        self.frame_7_button_dir = QPushButton(self.frame_7)
        self.frame_7_button_dir.setObjectName("but")
        self.frame_7_button_dir.setText("Select")
        self.frame_7_button_dir.move(200,280)
        self.frame_7_button_dir.clicked.connect(self.img_select)
        
        self.frame_7_button = QPushButton(self.frame_7)
        self.frame_7_button.setObjectName("login_B")
        self.frame_7_button.setText("Start")
        self.frame_7_button.move(100,340)
        self.frame_7_button.clicked.connect(self.img_car)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_7)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
#part 7...................................................................................
        self.button_7 = QPushButton(self.first_frame)
        self.button_7.setObjectName("button_1")
        self.button_7.setText("  Car Detection 2 ")              
        self.button_7.move(50,400)
        self.button_7.clicked.connect(self.car_live)
        
        #eighth frame
        self.frame_8 = QFrame(self)
        self.frame_8.setObjectName("frame_2")
        self.frame_8.move(100,100)
        self.frame_8.setVisible(False)
        
        self.frame_8_head = QLabel(self.frame_8)
        self.frame_8_head.setObjectName("heading")
        self.frame_8_head.setText("Live Car Detection")
                                  
        self.frame_8_head.move(70,30)
        
        self.frame_8_text = QLabel(self.frame_8)
        self.frame_8_text.setObjectName("text")
        self.frame_8_text.setText("\n\nClick on start to activate\nDog/Cat Classifier function\n\n\nPress Enter To Exit \nPopUp Window")
        self.frame_8_text.move(50,100)
        
        self.frame_8_box = QLineEdit(self.frame_8)
        self.frame_8_box.setObjectName("line_edit")
        self.frame_8_box.setText("Select Image Location")
        self.frame_8_box.move(30,280)
        
        self.frame_8_button_dir = QPushButton(self.frame_8)
        self.frame_8_button_dir.setObjectName("but")
        self.frame_8_button_dir.setText("Select")
        self.frame_8_button_dir.move(200,280)
        self.frame_8_button_dir.clicked.connect(self.vid_select)
        
        self.frame_8_button = QPushButton(self.frame_8)
        self.frame_8_button.setObjectName("login_B")
        self.frame_8_button.setText("Start")
        self.frame_8_button.move(100,340)
        self.frame_8_button.clicked.connect(self.live_car)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_8)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
        
#part 8...................................................................................
        self.button_8 = QPushButton(self.first_frame)
        self.button_8.setObjectName("button_1")
        self.button_8.setText("  Age Classifier ")                    
        self.button_8.move(250,400)
        self.button_8.clicked.connect(self.age)
        
        #ninth window
        self.frame_9 = QFrame(self)
        self.frame_9.setObjectName("frame_2")
        self.frame_9.move(100,100)
        self.frame_9.setVisible(False)
        
        self.frame_9_head = QLabel(self.frame_9)
        self.frame_9_head.setObjectName("heading")
        self.frame_9_head.setText("  Age Classifier ")
        self.frame_9_head.move(70,30)
        
        self.frame_9_text = QLabel(self.frame_9)
        self.frame_9_text.setObjectName("text")
        self.frame_9_text.setText("\n\nClick on start to activate\nAge Classifier function\n\n\nPress Enter To Exit \nPopUp Window")
        self.frame_9_text.move(50,100)
        
        self.frame_9_button = QPushButton(self.frame_9)
        self.frame_9_button.setObjectName("login_B")
        self.frame_9_button.setText("Start")
        self.frame_9_button.move(100,340)
        self.frame_9_button.clicked.connect(self.age_up)
        
        
        #back Button
        
        self.back_1 = QLabel(self.frame_9)
        self.back_1.setTextFormat(Qt.RichText)
        self.back_1.setObjectName("back")
        self.back_1.setText("&#8592")
        self.back_1.move(20,10)
        self.back_1.mousePressEvent = self.my_back
        
   
        self.show()
        
        
#function definations for back and forward moment 
    def mask(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Mask Detection")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(True)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Mask.mp3")
    
    def face(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Face Classifier")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(True)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Face_Classifier.mp3")
    
    def img_obj(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Image Oject Detection")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(True)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Img_Obj_Det.mp3")
        
        
    def live_obj(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Live Object Detection")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(True)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Liv_Obj_Det.mp3")
        
        
    def social(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Social Distincing")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(True)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Social_di.mp3")
    
    def car_img(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Image Car Detection")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_7.setVisible(True)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        playsound("Sounds/Car_Det.mp3")
    
    def car_live(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Live Car Detection")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(True)
        self.frame_9.setVisible(False)
        playsound("Sounds/Cam_Car_Det.mp3")
        
    def age(self):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Age Classifier")
        self.first_frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(True)
        playsound("Sounds/Age_Det.mp3")
        

                

    def my_back(self,event):
        self.login_window1.setVisible(False)
        self.statusBar().showMessage("Services")
        self.first_frame.setVisible(True)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)
        self.frame_6.setVisible(False)
        self.frame_7.setVisible(False)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        
        
        
#function perfroming tasks

    def register(self):
        try:
            
            from Face_Recognition_Login import registration
            reg = registration()
            reg.register_function()
            self.login_window.setVisible(False)
            self.login_window1.setVisible(True)
        except:
            self.text_q = QLabel(self.login_window)
            self.text_q.setObjectName("text")
            self.text_q.setText("Something Went Wrong")
            self.text_q.move(30,250)
            
    
    def login(self):
        from Face_Recognition_Login import registration
        log = registration
        log = log.login_function(self)
        if log ==1:
            self.login_window1.setVisible(False)
            self.statusBar().showMessage("Service")
            self.first_frame.setVisible(True)
            self.frame_2.setVisible(False)
            self.frame_3.setVisible(False)
            self.frame_4.setVisible(False)
            self.frame_5.setVisible(False)
            self.frame_6.setVisible(False)
            self.frame_7.setVisible(False)
            self.frame_8.setVisible(False)
            self.frame_9.setVisible(False)
            playsound("Sounds/User.mp3")
        else:
            self.name_q1.setText("User Not Find")
            
        
    def delete_all(self):
        try:
            k =os.listdir("Images/")
            for i in k[1:]:
                os.remove("Images/{}".format(i))
            self.text_q1.setText("Close Application")
            self.text_q1.move(30,200)
        except:
            self.text_q1.setText("SomeThing Went Wrong")
            self.text_q1.move(30,200)
            
    def mask_detection(self):
        from maskdetection import md
        de = md()
        de = de.detection()
        if de:
            pass
        else:
            self.frame_2_text.setText("\n\nSomething Went Wrong")
            self.frame_2_text.move(50,100)
    def face_classifier(self):
        from FaceDetection import fd
        de = fd()
        de = de.face()
        if de:
            pass
        else:
            self.frame_3_text.setText("\n\nSomething Went Wrong")
            self.frame_3_text.move(50,100)
            
    def img_class(self):
        from ImageDetection import ImgD
        de = ImgD()
        try:
            img_path = self.fileName
            de = de.img_det(img_path)
            if de:
                pass
            else:
                self.frame_4_text.setText("\n\nSomething Went Wrong")
                self.frame_4_text.move(50,100)
        except:
            self.frame_4_box.setText("Select Proper Image")
            
            
    def img_select(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self,"Select File", "","jpg Files (*.jpg);;png Files (*.png)")
        self.frame_4_box.setText(self.fileName)
        self.frame_6_box.setText(self.fileName)
        self.frame_7_box.setText(self.fileName)
    
    def vid_select(self):
        self.vid_file, _ = QFileDialog.getOpenFileName(self,"Select File", "","MP4 Files (*.mp4)")
        self.frame_8_box.setText(self.vid_file)
    
    
    def liv_det(self):
        from ImageDetection import ImgD
        de = ImgD()
        de = de.live_det()
        if de:
            pass
        else:
            self.frame_5_text.setText("\n\nSomething Went Wrong")
            self.frame_5_text.move(50,100)
    def social_distance(self):
        from Social_Distance import sd
        de = sd()
        try:
            de = de.sosi_di(self.fileName)
            if de:
                pass
            else:
                self.frame_6_text.setText("\n\nSomething Went Wrong")
                self.frame_6_text.move(50,100)
        except:
            self.frame_6_box.setText("Select Proper Image")

        
    
    def img_car(self):
        from Car_Detection import cd
        de = cd()
        try:
            de = de.car_img_de(self.fileName)
            if de:
                pass
            else:
                self.frame_7_text.setText("\n\nSomething Went Wrong")
                self.frame_7_text.move(50,100)
        except:
            self.frame_7_box.setText("Select Proper Image")
        
        
    def live_car(self):
        from Car_Detection import cd
        de = cd()
        try:
            de = de.car_live_de(self.vid_file)
            
            if de:
                pass
            else:
                self.frame_8_text.setText("\n\nSomething Went Wrong")
                self.frame_8_text.move(50,100)
        except:
            self.frame_8_box.setText("Select Proper Video")
            
    def age_up(self):
        from Age_Detection import ad
        de = ad()
        de = de.age_det()
        if de:
            pass
        else:
            self.frame_9_text.setText("\n\nSomething Went Wrong")
            self.frame_9_text.move(50,100)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
    app.quit()


# In[ ]:




