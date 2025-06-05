from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Help:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Disk")

        #First image
        img1 = Image.open("college_images\\helpDesk.png")
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


         # Outer Frame (Thick Border Effect)
        left_main_frame = Frame(bg_img, bg="#FFCA02", bd=2)  # Thicker border
        left_main_frame.place(x=520, y=150, width=500, height=150)  # Slightly larger than inner frame

        # Inner Frame
        Left_frame = Frame(left_main_frame, bg="#072E59")
        Left_frame.place(x=2, y=2, width=492, height=142)  # Smaller and inset inside outer frame

        email_label = Label(Left_frame, text="Email: 212012@kit.ac.in", font=("Helvetica", 30, "bold"), bg="#072E59", fg="white")
        email_label.grid(row=2,column=0,padx=10,pady=6,sticky=W)

        email_label = Label(Left_frame, text="Email: 222092@kit.ac.in", font=("Helvetica", 30, "bold"), bg="#072E59", fg="white")
        email_label.grid(row=3,column=0,padx=10,pady=6,sticky=W)




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()