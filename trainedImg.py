from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class TrainedImg:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Trained Data Sets")
        
        #First image
        img1 = Image.open("college_images\\trainedDataSet.png")
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
        
        # #Button
        btn_frame1 = Frame(bg_img, bd=2, relief=RIDGE, bg="#FFCA02")
        btn_frame1.place(x=20, y=520 , width=1480 , height=70)
        
        take_photo_btn = Button(btn_frame1,text="TRAINED DATA",command=self.train_classifier,font=("Helvetica", 13, "bold"),bg="#072E59", fg="white",width=145,height=2)
        take_photo_btn.grid(row=0,column=0,padx=7,pady=7,sticky=W)
        # b1_1 = Button(bg_img,text="Trained Data",cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        # b1_1.place(x = 20 , y = 520 , width = 1480 , height = 60)
        
    def train_classifier(self):
        data_dir = ("data")
        path = [ os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert("L") #Gray scale IMAGE
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)
        
        #------------Train The classifier and Save--------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training Completed","The trained model has been saved successfully.",parent=self.root)
                        
if __name__ == "__main__":
    root = Tk()
    obj = TrainedImg(root)
    root.mainloop()