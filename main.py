from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from trainedImg import TrainedImg
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Attendance Management System while using Face Recognition")
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")

        #First image
        img1 = Image.open("college_images\\faceRecognition.png")
        img1= img1.resize((1550,130),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0 , y=0   , width=1550 , height=130)

        
        
        #BG bg_img
        img4 = Image.open("college_images\\bgImg.png")
        img4 = img4.resize((1536,710),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root,image = self.photoimg4)
        bg_img.place(x=0 , y=130  , width=1536, height=710)


         #---------------Date Function Button-------------------------------------------
 
        def show_date():
            date_string = strftime('%B %d, %Y')  # Example: May 21, 2025
            date_lbl.config(text=date_string)
            date_lbl.after(60000, show_date)  # Update every 60 seconds (date usually changes daily)

        date_lbl = Label(bg_img, font=("Helvetica", 18, "bold"), bg="#072E59", fg="white", bd=4,relief="groove")
        date_lbl.grid(row=20, column=135, padx=10, pady=5, sticky="w")
        show_date()
        
        
        #---------------Time Function Button-------------------------------------------
        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
    
        
        lbl = Label(bg_img, font=("Helvetica", 18, "bold"), bg="#072E59", fg="white",bd=4,relief="groove")
        lbl.grid(row=20,column=136,padx=10,pady=5,sticky=W)
        time()

        
        #Student details Button
        img5 = Image.open("college_images\\students.png")
        img5 = img5.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image = self.photoimg5,command=self.student_details,cursor = "hand2",bg = "black")
        b1.place(x = 200 , y = 100 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x = 200 , y = 300 , width = 220 , height = 40)
        
        
        
        #Detect Face Button
        img6 = Image.open("college_images\\faceDetect.png")
        img6 = img6.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img,image = self.photoimg6,command=self.face_data,cursor = "hand2",bg = "black")
        b1.place(x = 500 , y = 100 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Face Detector",command=self.face_data,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x = 500 , y = 300 , width = 220 , height = 40)
       
       
       
        #Attendance  Button
        img7 = Image.open("college_images\\attendance.png")
        img7 = img7.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img,image = self.photoimg7,command=self.attendance_data,cursor = "hand2",bg = "black")
        b1.place(x = 800 , y = 100 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Attendance",command=self.attendance_data,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x =800 , y = 300 , width = 220 , height = 40)
        
        
        
        #Help Button
        img8 = Image.open("college_images\\help.png")
        img8 = img8.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img,image = self.photoimg8,command=self.help_data,cursor = "hand2",bg = "black")
        b1.place(x = 1100 , y = 100 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Help Desk",command=self.help_data,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x =1100 , y = 300 , width = 220 , height = 40)
        
        
        
        #Trained Button
        img9 = Image.open("college_images\\trainedData.png")
        img9 = img9.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img,image = self.photoimg9,command=self.train_data,cursor = "hand2",bg = "black")
        b1.place(x = 200 , y = 380 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Trained Data",command=self.train_data,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x =200 , y = 580 , width = 220 , height = 40)
        
        
        
         #Photos Button
        img10 = Image.open("college_images\\photos.png")
        img10 = img10.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img,image = self.photoimg10,command=self.open_img,cursor = "hand2",bg = "black")
        b1.place(x = 500 , y = 380 , width = 220 , height = 220)
        
        b1_1 = Button(bg_img,text="Photos",command=self.open_img,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x = 500 , y = 580 , width = 220 , height = 40)
        
        
        
        #Developer Button
        img11 = Image.open("college_images\\developer.png")
        img11 = img11.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img,image = self.photoimg11,command=self.developer_data,cursor = "hand2",bg = "black")
        b1.place(x = 800 , y = 380 , width = 220 , height = 220)
        b1_1 = Button(bg_img,text="Developer",command=self.developer_data,cursor = "hand2" ,font=("Helvetica", 15, "bold"), bg="#072E59", fg="white")
        b1_1.place(x = 800 , y = 580 , width = 220 , height = 40)
        
        
        
        #Exit Button
        img12 = Image.open("college_images\\exits.png")
        img12= img12.resize((220,220),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b1 = Button(bg_img,image = self.photoimg12,command=self.iExit,cursor = "hand2",bg = "black")
        b1.place(x = 1100 , y = 380 , width = 220 , height = 220)

        b1_1 = Button(bg_img,text="Exit",command=self.iExit,cursor = "hand2" ,font=("Helvetica", 15, "bold"),bg="#072E59", fg="white")
        b1_1.place(x = 1100 , y = 580 , width = 220 , height = 40)
    
    
    
    #---------------Open Image ---------------------------------------------------
    def open_img(self):
        os.startfile("data")

    #---------------Exit Function Button---------------------------------------------------
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else :
            return
        


    #-------------------------------Functions Buttons------------------------------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    #-------------------------------Training Buttons------------------------------
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainedImg(self.new_window)
        
    #---------------------Face Recognition ----------------------------------------
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    #---------------------Attendance Detail ----------------------------------------
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    #---------------------Developer ----------------------------------------
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

  #---------------------Help Desk ----------------------------------------
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()