from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        
        self.root = root
        # Used to crete the FaceRecognition window object
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Managment System")
        
        
        #------------------Variables --------------------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
       
        
        
        #First image
        img1 = Image.open("college_images\\studentManagment.png")
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
        frame_label = Label(Left_frame, text="Student Details", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        frame_label.grid(row=0,column=0)
        
        
        img_left = Image.open("college_images\\studentsDetails.png")
        img_left = img_left.resize((747,130),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=4 , y=20 , width=745 , height=130)
        
        #current course Info Frame
        # Updated code
        current_course_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="#072E59")
        current_course_frame.place(x=4, y=155 , width=745 , height=200)
        # Add a Label to show the "Student Details" text
        label = Label(current_course_frame, text="Current Course Information", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        label.grid(row=0,column=0)
        
        # Department Label and ComboBox in Left Frame
        dep_label = Label(current_course_frame, text="Department", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        dep_label.grid(row=1,column=0,padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame,textvariable = self.var_dep , font=("Helvetica", 12, "bold"),state="readonly",width=17)
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "AIML", "Mechanical","Electrical")
        dep_combo.current(0)  # Set the default value
        dep_combo.grid(row=1,column=1,padx=2,pady=10)  # Using pack here
        
        
        
        # Course and ComboBox in Left Frame
        course_label = Label(current_course_frame, text="Course", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        course_label.grid(row=1,column=2,padx=10,sticky=W) # Set the default value)
        
        course_combo = ttk.Combobox(current_course_frame, textvariable = self.var_course ,font=("Helvetica", 12, "bold"),state="readonly",width=17)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)  # Set the default value
        course_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)  # Using pack here
       
       
       
        # Year and ComboBox in Left Frame
        year_label = Label(current_course_frame, text="Year", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        year_label.grid(row=2,column=0,padx=10,sticky=W) # Set the default value)
        
        year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_year ,font=("Helvetica", 12, "bold"),state="readonly",width=17)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)  # Set the default value
        year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)  # Using pack here
        
        
        
        # Semester and ComboBox in Left Frame
        semeter_label = Label(current_course_frame, text="Semester", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        semeter_label.grid(row=2,column=2,padx=10,sticky=W) # Set the default value)
        
        semeter_combo = ttk.Combobox(current_course_frame,textvariable = self.var_semester , font=("Helvetica", 12, "bold"),state="readonly",width=17)
        semeter_combo["values"] = ("Select Semester", "Semester-1", "Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semeter_combo.current(0)  # Set the default value
        semeter_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)  # Using pack here
        
        # Class Student Information Frame 
        # Updated code
        class_Student_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="#072E59")
        class_Student_frame.place(x=4, y=280 , width=745 , height=310)
        # Add a Label to show the "Student Details" text
        label = Label(class_Student_frame, text="Class Student Information", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        label.grid(row=0,column=0)
        
        
        #StudentId and Entry in Left Frame
        studentId_label = Label(class_Student_frame, text="Student Id:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        studentId_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        studentID_entry = ttk.Entry(class_Student_frame,textvariable = self.var_std_id , font=("Helvetica", 12, "bold"), width=20)
        studentID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        #StudentName and Entry in Left Frame
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        studentName_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        studentName_entry = ttk.Entry(class_Student_frame, textvariable = self.var_std_name ,font=("Helvetica", 12, "bold"), width=20)
        studentName_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        
        #Class Devision and Entry in Left Frame
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        class_div_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) # Set the default value)
        
        div_combo = ttk.Combobox(class_Student_frame,textvariable = self.var_div , font=("Helvetica", 12, "bold"),state="readonly",width=18)
        div_combo["values"] = ("Select Division", "A", "B","C")
        div_combo.current(0)  # Set the default value
        div_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        # class_div_entry = ttk.Entry(class_Student_frame, textvariable = self.var_div ,font=("Helvetica", 12, "bold"), width=20)
        # class_div_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        
        # Roll No. and Entry in Left Frame
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        roll_no_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        roll_no_entry = ttk.Entry(class_Student_frame, textvariable = self.var_roll ,font=("Helvetica", 12, "bold"), width=20)
        roll_no_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        
        # Gender and Entry in Left Frame
        gender_label = Label(class_Student_frame, text="Gender:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        gender_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        gender_combo = ttk.Combobox(class_Student_frame,textvariable = self.var_gender , font=("Helvetica", 12, "bold"),state="readonly",width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female","Other")
        gender_combo.current(0)  # Set the default value
        gender_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        # gender_entry = ttk.Entry(class_Student_frame, textvariable = self.var_gender ,font=("Helvetica", 12, "bold"), width=20)
        # gender_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        # DOB and Entry in Left Frame
        dob_label = Label(class_Student_frame, text="DOB:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        dob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        dob_entry = ttk.Entry(class_Student_frame, textvariable = self.var_dob,font=("Helvetica", 12, "bold"), width=20)
        dob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        
        # Email and Entry in Left Frame
        email_label = Label(class_Student_frame, text="Email:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        email_label.grid(row=4,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        email_entry = ttk.Entry(class_Student_frame, textvariable = self.var_email ,font=("Helvetica", 12, "bold"), width=20)
        email_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        # Phone No. and Entry in Left Frame
        phone_label = Label(class_Student_frame, text="Phone No:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        phone_label.grid(row=4,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        phone_entry = ttk.Entry(class_Student_frame, textvariable = self.var_phone ,font=("Helvetica", 12, "bold"), width=20)
        phone_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        
        # Address and Entry in Left Frame
        address_label = Label(class_Student_frame, text="Address:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        address_label.grid(row=5,column=0,padx=10,pady=5,sticky=W) # Set the default value)\
        
        address_entry = ttk.Entry(class_Student_frame, textvariable = self.var_address ,font=("Helvetica", 12, "bold"), width=20)
        address_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        # Teacher and Entry in Left Frame
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        teacher_label.grid(row=5,column=2,padx=10,pady=5,sticky=W) # Set the default value)\
        
        teacher_entry = ttk.Entry(class_Student_frame, textvariable = self.var_teacher ,font=("Helvetica", 12, "bold"), width=20)
        teacher_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)  # Using pack here
        
        
        #Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable = self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        
        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable = self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=7,column=1,padx=10,pady=5,sticky=W)
        
        
        # Button Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="#072E59")
        btn_frame.place(x=7, y=230 , width=708 , height=35)
        #buttons
        save_btn = Button(btn_frame,text="Save",command=self.add_data,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        save_btn.grid(row=0,column=0,padx=1,pady=1,sticky=W)
        
        update_btn = Button(btn_frame,text="Update",command=self.update_data,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        update_btn.grid(row=0,column=1,padx=1,pady=1,sticky=W)
        
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        delete_btn.grid(row=0,column=2,padx=1,pady=1,sticky=W)
        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=17)
        reset_btn.grid(row=0,column=3,padx=1,pady=1,sticky=W)
        
        # Button Frame
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="#072E59")
        btn_frame1.place(x=7, y=265 , width=708 , height=35)
        
        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=35)
        take_photo_btn.grid(row=0,column=0,padx=2,pady=1,sticky=W)
        
        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",font=("Helvetica", 12, "bold"),bg="#FFCA02", fg="Black",width=35)
        update_photo_btn.grid(row=0,column=1,padx=2,pady=1,sticky=W)
        
        # ------------------------------------------------------Left Frame End-----------------------------------------------------
       
        # ------------------------------------------------------Right Frame Start--------------------------------------------------
        
        # Right Frame without 'text' and 'font'
        Right_frame = Frame(main_frame, bd=2, bg="#072E59", relief=RIDGE)
        Right_frame.place(x=780, y=10, width=715,  height=600)
        # Add a Label for "Student Details" inside the frame
        frame_label = Label(Right_frame, text="Student Details", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        frame_label.grid(padx=0, pady=0)
        
        img_right = Image.open("college_images\\studentsDetails1.png")
        img_right = img_right.resize((747,130),Image.LANCZOS) #Lanczos used to convert High Level Images to low level images
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=4 , y=20 , width=700 , height=130)
        
        #--------------------------------------------------------Searching System Frame-----------------------------------------------
        
        Search_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#072E59")
        Search_frame.place(x=4, y=155 , width=701 , height=90)
        # Add a Label to show the "Student Details" text
        label = Label(Search_frame, text="Search System", font=("Helvetica", 10, "bold"), bg="#072E59", fg="white")
        label.grid(row=0,column=0)
        
        # Search and comboBox in Left Frame
        search_label = Label(Search_frame, text="Search By: ", font=("Helvetica", 12, "bold"), bg="#072E59", fg="white")
        search_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) # Set the default value
        
        search_combo = ttk.Combobox(Search_frame, font=("Helvetica", 11, "bold"),state="readonly",width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)  # Set the default value
        search_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)  # Using pack here
        
        search_entry = ttk.Entry(Search_frame, font=("Helvetica", 12, "bold"), width=15)
        search_entry.grid(row=1,column=2,padx=10,pady=5,sticky=W)  # Using pack here
        
        search_btn = Button(Search_frame,text="Search",font=("Helvetica", 9, "bold"),bg="#FFCA02", fg="Black",width=15)
        search_btn.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        showAll_btn = Button(Search_frame,text="Show All",font=("Helvetica", 9, "bold"),bg="#FFCA02", fg="Black",width=15)
        showAll_btn.grid(row=1,column=4,padx=5,pady=5,sticky=W)
        
        
        #--------------------------------------------------------Table Frame-----------------------------------------------
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#072E59")
        table_frame.place(x=4, y=250 , width=701 , height=340)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("div",width="100")
        self.student_table.column("roll",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phone",width="100")
        self.student_table.column("address",width="100")
        self.student_table.column("teacher",width="100")
        self.student_table.column("photo",width="120")
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ------------------------------------------------------Right Frame End-----------------------------------
        
    # ----------------------------------------------------Function Declaration--------------------------------
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else :
            #---------------------Store Data into DataBase------------------------------
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    #------------------------------Fetch Data From Databases--------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        
        if len(data) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()           
     
    #----------------------------Get Cursor From Databases or show data on system--------------------------------
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #------------------------------Update Data From Databases--------------------------------   
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else :
            try :
                Update = messagebox.askyesno("Update","Do you want to update student's data?",parent=self.root)
                if Update > 0 :
                    conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s , Division=%s,Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else :
                    if not Update :
                        return 
                messagebox.showinfo("Success","Student's Data Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #-------------------DeleteStudent Data----------------------------------------------------
    def delete_data(self):
        if self.var_std_id.get() == "" :
            messagebox.showerror("Error","Student ID is Required to delete",parent=self.root)
        else :
            try :
                delete = messagebox.askyesno("Delete","Do you want to delete this student's data ?",parent=self.root)
                if delete > 0 :
                    conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE Student_id=%s",(self.var_std_id.get(),))
                else :
                    if not delete :
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student's Data Deleted Successfully",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #---------------------------Reset Data--------------------------------------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.fetch_data()

    #--------------------------Generate Data or Take Photo Sample---------------
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else :
            try :
                conn = mysql.connector.connect(host="localhost",username="root",password="k05137849@K",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1 
                my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s , Division=%s,Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()     
                
                #----------------------------Load Predifined Data on face frontals from opencv ------------------------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaleFactor=1.3, minNeighbors=5
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                #to open Web camera we used 0 otherwise 1 for other camera or we can also give 
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face", face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 100 :
                        break
                 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Face Samples Generated Successfully",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()