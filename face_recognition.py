from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")
        
        #First image
        img1 = Image.open("college_images\\faceRecognitionHeading.png")
        img1= img1.resize((1550,130),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0 , y=0   , width=1550 , height=130)
        
        #BG bg_img
        img4 = Image.open("college_images\\bgImg.png")
        img4 = img4.resize((1536,710),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0 , y=130 , width=1536, height=710)
        
        
        #Face Detect Button
        img = Image.open("college_images\\faceDetection.png")
        img = img.resize((350,450),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg = ImageTk.PhotoImage(img)
        
        b1 = Button(bg_img,image = self.photoimg,command=self.face_recog,cursor = "hand2",bg = "black")
        b1.place(x = 590 , y = 80 , width = 350 , height = 450)
        # b1.place(x = 200 , y = 100 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Face Detect",command=self.face_recog,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x = 590 , y = 530 , width = 350 , height = 40)
        # b1_1.place(x = 200 , y = 300 , width = 450 , height = 40)
        
    #---------------------------Attendance ------------------------------------
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv", "r+",newline="\n") as f :
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%I:%M:%S %p")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                
                
                
                
    #---------------------------Face Recognition function------------------------
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0,255,0), 3)
                id,predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT Name FROM student WHERE Student_id =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id =" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("SELECT Dep FROM student WHERE Student_id =" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id =" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                if confidence > 70 :
                    cv2.putText(img,f"Student Id: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else :
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face Detected", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(img,"Unknown Face Detected",cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord = [x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        
        while True :
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
                       
                        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()