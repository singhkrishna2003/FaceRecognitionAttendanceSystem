from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[] #Global List to insert data from csv file




class Attendance:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Detail")
        
        #------------------------Variables----------------------------------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()






        #First image
        img1 = Image.open("college_images\\attendanceHeading.png")
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
        
         # Main Frame
        main_frame = Frame(bg_img , bd = 2 , bg = "#FFCA02")
        main_frame.place(x=10 , y=32 , width=1510 , height=650)
        
       # ------------------------------------------------------Left Frame Start--------------------------------------------------
    
        # Left_frame = Frame(main_frame, bd = 2, bg="#072E59",relief = RIDGE , text = "Student Details" , font=("Helvetica", 12, "bold")) 
        # Left_frame.place(x=10, y=10 , width=760 , height=580)
    
        # Left Frame without 'text' and 'font'
        Left_frame = Frame(main_frame, bd=2, bg="#072E59", relief=RIDGE)
        Left_frame.place(x=10, y=10, width=760, height=600)
        # Add a Label for "Student Details" inside the frame
        frame_label = Label(Left_frame, text="Student Attendance Details", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        frame_label.grid(row=0,column=0)
        
        img_left = Image.open("college_images\\studentInfo.png")
        img_left = img_left.resize((747,140),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=4 , y=20 , width=745 , height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="#072E59")
        left_inside_frame.place(x=4, y=150 , width=747 , height=430)
        # Add a Label to show the "Student Details" text
        # label = Label(left_inside_frame, text="Student Attendance Information", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        # label.grid(row=0,column=0)
        
        #AttendanceId and Entry in Left Frame
        attendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        attendanceId_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id,font=("Helvetica", 12, "bold"), width=20)
        attendanceID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)  # Using pack here

        #Roll No. and Entry in Left Frame
        rollLabel_label = Label(left_inside_frame, text="Roll No:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        rollLabel_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,font=("Helvetica", 12, "bold"), width=20)
        atten_roll.grid(row=1,column=3,padx=10,pady=5,sticky=W)  # Using pack here


        #StudentName and Entry in Left Frame
        nameLabel = Label(left_inside_frame, text="Student Name:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        nameLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        atten_name = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,font=("Helvetica", 12, "bold"), width=20)
        atten_name.grid(row=2,column=1,padx=10,pady=5,sticky=W)  # Using pack here


        # Department Label and ComboBox in Left Frame
        depLabel = Label(left_inside_frame, text="Department:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        depLabel.grid(row=2,column=2,padx=10, pady=5,sticky=W)

        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("Helvetica", 12, "bold"), width=20)
        atten_dep.grid(row=2,column=3,padx=10,pady=5,sticky=W)  # Using pack here


        # Time Label and ComboBox in Left Frame
        timeLabel = Label(left_inside_frame, text="Time:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        timeLabel.grid(row=3,column=0,padx=10,pady=5, sticky=W)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,font=("Helvetica", 12, "bold"), width=20)
        atten_time.grid(row=3,column=1,padx=10,pady=5,sticky=W)  # Using pack here


        # Date Label and ComboBox in Left Frame
        dateLabel = Label(left_inside_frame, text="Date:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        dateLabel.grid(row=3,column=2,padx=10, pady=5,sticky=W)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,font=("Helvetica", 12, "bold"), width=20)
        atten_date.grid(row=3,column=3,padx=10,pady=5,sticky=W)  # Using pack here

        #Attendance
        dep_label = Label(left_inside_frame, text="Attendance Status:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        dep_label.grid(row=4,column=0,padx=10,pady=5, sticky=W)
        
        dep_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,font=("Helvetica", 12, "bold"),state="readonly",width=18)
        dep_combo["values"] = ("Status", "Present", "Absent")
        dep_combo.grid(row=4,column=1,padx=10,pady=5)  # Using pack here
        dep_combo.current(0)  # Set the default value


        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="#072E59")
        btn_frame.place(x=10, y=370 , width=708 , height=35)
        #buttons
        save_btn = Button(btn_frame,text="Import csv",command=self.importCsv,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        save_btn.grid(row=0,column=0,padx=1,pady=1,sticky=W)
        
        update_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        update_btn.grid(row=0,column=1,padx=1,pady=1,sticky=W)
        
        delete_btn = Button(btn_frame,text="Update",font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        delete_btn.grid(row=0,column=2,padx=1,pady=1,sticky=W)
        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        reset_btn.grid(row=0,column=3,padx=1,pady=1,sticky=W)




        # ------------------------------------------------------Left Frame End-----------------------------------------------------
       
        # ------------------------------------------------------Right Frame Start--------------------------------------------------
        
        # Right Frame without 'text' and 'font'
        Right_frame = Frame(main_frame, bd=2, bg="#072E59", relief=RIDGE)
        Right_frame.place(x=780, y=10, width=715,  height=600)
        
        # Add a Label for "Student Details" inside the frame
        frame_label = Label(Right_frame, text="Student Details", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        frame_label.grid(padx=0, pady=0)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#072E59")
        table_frame.place(x=4, y=22 , width=701 , height=553)
        
        # ------------------------------------------------------Scroll Bar Table--------------------------------------------------

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
       
        
        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        self.AttendanceReportTable["show"] = "headings"

        
        self.AttendanceReportTable.column("id",width="100")
        self.AttendanceReportTable.column("roll",width="100")
        self.AttendanceReportTable.column("name",width="100")
        self.AttendanceReportTable.column("dep",width="100")
        self.AttendanceReportTable.column("time",width="100")
        self.AttendanceReportTable.column("date",width="100")
        self.AttendanceReportTable.column("attendance",width="120")
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        

 #------------------------------Fetch Data From Databases--------------------------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


#------------------------------------Import Csv-------------------------------------------  
#------------------------------------Import Data from Csv File which is already you have---------------------------------------
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

#------------------------------------Export Csv-------------------------------------------  
#------------------------------------Export Data to Csv File which is newly created---------------------------------------
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),parent=self.root, defaultextension=".csv")
            with open(fln, mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported  to "+os.path.basename(fln)+" successfully")
        
        except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


 #----------------------------Get Cursor From Databases or show data on system--------------------------------

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



#---------------------------Reset Data--------------------------------------------------
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()