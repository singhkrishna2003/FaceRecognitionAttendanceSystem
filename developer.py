from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        #First image
        img1 = Image.open("college_images\\developers.png")
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

       #-------------------------------------------------Krishna Singh-------------------------------------------------------
        img = Image.open("college_images\\singhkrishnna.png")
        img = img.resize((350, 450), Image.LANCZOS)
        self.photoimg_krishna = ImageTk.PhotoImage(img)  # Unique variable

        b1 = Button(bg_img, image=self.photoimg_krishna,cursor = "hand2",bg = "black")
        b1.place(x=150, y=23, width=350, height=450)

       # Outer Frame (Thick Border Effect)
        left_main_frame = Frame(bg_img, bg="#FFCA02", bd=2)  # Thicker border
        left_main_frame.place(x=150, y=490, width=350, height=140)  # Slightly larger than inner frame

        # Inner Frame
        Left_frame = Frame(left_main_frame, bg="#072E59")
        Left_frame.place(x=2, y=2, width=342, height=132)  # Smaller and inset inside outer frame

        name_label = Label(Left_frame, text="Name: Krishna Singh", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        name_label.grid(row=0,column=0,padx=30,pady=5,sticky=W) # Set the default value)

        roll_label = Label(Left_frame, text="RollNo: 2101650130004", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        roll_label.grid(row=1,column=0,padx=30,pady=5,sticky=W)

        email_label = Label(Left_frame, text="Email: 212012@kit.ac.in", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        email_label.grid(row=2,column=0,padx=30,pady=5,sticky=W)

        # ---------------------------------------------------Akash Yadav---------------------------------------------------------
        img1 = Image.open("college_images\\Akash.jpg")
        img1 = img1.resize((350, 450), Image.LANCZOS)
        self.photoimg_akash = ImageTk.PhotoImage(img1)  # Another unique variable

        b2 = Button(bg_img, image=self.photoimg_akash,cursor = "hand2",bg = "black")
        b2.place(x=1000, y=20, width=350, height=450)

        # Outer Frame (Thick Border Effect)
        right_main_frame = Frame(bg_img, bg="#FFCA02", bd=2)  # Thicker border
        right_main_frame.place(x=1000, y=490, width=350, height=140)  # Slightly larger than inner frright
        # Inner Frame
        right_frame = Frame(right_main_frame, bg="#072E59")
        right_frame.place(x=2, y=2, width=342, height=132)  # Smaller and inset inside outer frame

        name_label = Label(right_frame, text="Name: Akash Yadav", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        name_label.grid(row=0,column=0,padx=30,pady=5,sticky=W) # Set the default value)

        roll_label = Label(right_frame, text="RollNo: 2201650139001", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        roll_label.grid(row=1,column=0,padx=30,pady=5,sticky=W)

        email_label = Label(right_frame, text="Email: 222092@kit.ac.in", font=("Helvetica", 18, "bold"), bg="#072E59", fg="white")
        email_label.grid(row=2,column=0,padx=30,pady=5,sticky=W)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()