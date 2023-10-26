from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class StudentDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Security System")
        self.root.geometry("1751x790+0+0")

        #Variables
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_gender=StringVar()
        self.var_program=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_phone=StringVar()
 
        # cOVER IMAGE
        img1 = Image.open(r"D:\D drive\Python\Images\11.JPG")
        img1 = img1.resize((1751, 220), Image.LANCZOS)   
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1751, height=220)
 
        #Background_Image
        img4=Image.open(r"D:\D drive\Python\Images\13.JPG")  
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=210,width=1530,height=710)
 
        #Making of Frames
        main_frame=Frame(bg_img,bd=2) 
        main_frame.place(x=0,y=0,width=1350,height=500)

        #Left_Label_Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("archivo black",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=480)

        img_left=Image.open(r"D:\D drive\Python\Images\12.JPG")
        img_left=img_left.resize((660,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=100)

        #Current_Course_Frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("archivo black",12,"bold"))
        current_course_frame.place(x=5,y=100,width=650,height=100)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("archivo black",10),bg="white")
        year_label.grid(row=0,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("archivo black",10),state="readonly",width=17)
        year_combo["values"]=("Select Year","1st Year","2nd Year","3rd Year","4th Year")
        year_combo.current(0)
        year_combo.grid(row=0,column=1,padx=30,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("archivo black",10),bg="white")
        semester_label.grid(row=0,column=2,padx=0,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("archivo black",10),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=3,padx=12,pady=10,sticky=W)

        #Gender
        Gen_label=Label(current_course_frame,text="Gender",font=("archivo black",10),bg="white")
        Gen_label.grid(row=1,column=0,padx=10,sticky=W)

        Gen_combo=ttk.Combobox(current_course_frame,textvariable=self.var_gender,font=("archivo black",10),state="readonly",width=17)
        Gen_combo["values"]=("Male","Female","Not Specific" )
        Gen_combo.current(0)
        Gen_combo.grid(row=1,column=1,padx=30,pady=10,sticky=W)

        #program
        program_label=Label(current_course_frame,text="Program",font=("archivo black",10),bg="white")
        program_label.grid(row=1,column=2,padx=0,sticky=W)

        program_combo=ttk.Combobox(current_course_frame,textvariable=self.var_program,font=("archivo black",10),state="readonly",width=17)
        program_combo["values"]=("Select Program","Mphil","BS" )
        program_combo.current(0)
        program_combo.grid(row=1,column=3,padx=12,pady=10,sticky=W)
        
        

        #Class_Student_Information_Frame
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("archivo black",12,"bold"))
        class_Student_frame.place(x=5,y=200,width=650,height=200)
        
        #Student_ID
        studentID_label=Label(class_Student_frame,text="Student ID:",font=("archivo black",10),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("archivo black",10))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student_Name
        studentName_label=Label(class_Student_frame, text="Student Name:",font=("archivo black",10),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("archivo black",10))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Student_Division
        
        studentDivision_label=Label(class_Student_frame,text="Student Division:",font=("archivo black",10),bg="white")
        studentDivision_label.grid(row=1,column=0,padx=10,sticky=W)

        studentDivision_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=15,font=("archivo black",10))
        studentDivision_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #PhoneNO
        phoneNo_label=Label(class_Student_frame,text="Phone No:",font=("archivo black",10),bg="white")
        phoneNo_label.grid(row=1,column=2,padx=10,sticky=W)

        phoneNo_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=15,font=("archivo black",10))
        phoneNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #radio_button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=2,column=0)
  
        radiobutton2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=2,column=1)
 
        

        #button_frame
        button_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=100,width=650,height=50)

        #Save_button
        save_button=Button(button_frame,text="Save",width=10,font=("archivo black",10),bg="blue",fg="white", command=self.add_data)

        save_button.grid(row=0,column=0)

        #Update_button
        update_button=Button(button_frame,text="Update",width=10,font=("archivo black",10),bg="blue",fg="white",command=self.update_data)
        update_button.grid(row=0,column=1)

        #Delete_button
        delete_button=Button(button_frame,text="Delete",width=10,font=("archivo black",10),bg="blue",fg="white",command=self.delete_data)
        delete_button.grid(row=0,column=2)

        #Reset_button
        reset_button=Button(button_frame,text="Reset",width=10,font=("archivo black",10),bg="blue",fg="white",command=self.reset_data)
        reset_button.grid(row=0,column=3)

        #Take_Photo_button
        take_photo_button=Button(button_frame,text="Take Photo Sample",width=17,font=("archivo black",10),bg="blue",fg="white",command=self.generate_dataset)
        take_photo_button.grid(row=0,column=4)

        #Update_Photo_button
        update_photo_button=Button(button_frame,text="Update Photo Sample",width=17,font=("archivo black",10),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=5)

        #Right_frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("archivo black",12,"bold"))
        Right_frame.place(x=680,y=10,width=630,height=500)

        img_right=Image.open(r"D:\D drive\Python\Images\17.JPG")
        img_right=img_right.resize((660,100),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=100)


        #Search_System
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("archivo black",12,"bold"))
        search_frame.place(x=5,y=100,width=640,height=70)

        #Search_Label
        search_label=Label(search_frame,text="Search By:",font=("archivo black",10),bg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        #Search_combo
        search_combo=ttk.Combobox(search_frame,font=("archivo black",10),width=15,state="readonly")
        search_combo["values"]=("Select","Student_ID","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Search_entry
        search_entry=ttk.Entry(search_frame,width=15,font=("archivo black",10))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search_button
        search_button=Button(search_frame,text="Search",width=10,font=("archivo black",10),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=4)

        #ShowAll_button
        showAll_button=Button(search_frame,text="Show All",width=10,font=("archivo black",10),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4,padx=4)

        #Table_Frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=570,height=260)

        #Scroll_bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Year","Semester","Gender","Program","Student_ID","Student_name","Student_Division","Phone_No", ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Program",text="Program")
        self.student_table.heading("Student_ID",text="ID")
        self.student_table.heading("Student_name",text="Name")
        self.student_table.heading("Student_Division",text="Division")
        self.student_table.heading("Phone_No",text="Phone")
        self.student_table["show"]="headings"

        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Program",width=100)
        self.student_table.column("Student_ID",width=100)
        self.student_table.column("Student_name",width=100)
        self.student_table.column("Student_Division",width=100)
        self.student_table.column("Phone_No",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



     #function declaration
     
    def add_data(self):
        if self.var_year.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="20202023@ALI",database="myfyp")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_year.get(),
                                                                                          self.var_semester.get(),
                                                                                          self.var_gender.get(),
                                                                                          self.var_program.get(),
                                                                                          self.var_std_id.get(),
                                                                                          self.var_std_name.get(),
                                                                                          self.var_div.get(),
                                                                                          self.var_phone.get()
                                                                                         
                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

            #fetching data

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="20202023@ALI",database="myfyp")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

      #get_cursor  

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
   

        self.var_year.set(data[0]),
        self.var_semester.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_program.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_phone.set(data[7]),
        self.var_radio1.set("")


        #update function

    def update_data(self):
        if self.var_year.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="20202023@ALI",database="myfyp")
                    my_cursor=conn.cursor()
                    query = "UPDATE Student SET Year=%s, Semester=%s, Gender=%s, Program=%s, Student_Name=%s, Student_Division=%s, Phone_no=%s WHERE Student_ID=%s"
                    my_cursor.execute(query, (
                      

                                                                                                                                      self.var_year.get(),
                                                                                                                                      self.var_semester.get(),
                                                                                                                                      self.var_gender.get(),
                                                                                                                                      self.var_program.get(),
                                                                                                                                      self.var_std_name.get(),
                                                                                                                                      self.var_div.get(),
                                                                                                                                      self.var_phone.get(),
                                                                                                                                      self.var_std_id.get() 
                                                                                                                                 
                                                                                                                                        ) )
                           
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                                
                  
        #delete function
        
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="20202023@ALI",database="myfyp")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        #reset function

    def reset_data(self):
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_gender.set("Not Specific"),
        self.var_program.set("Select Program"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set (""),
        self.var_phone.set("")
        self.var_radio1.set("")
         



#Generate dataset or photo sample
    def generate_dataset(self):
        if self.var_year.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="20202023@ALI",database="myfyp")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                query = "UPDATE Student SET Year=%s, Semester=%s, Gender=%s, Program=%s, Student_Name=%s, Student_Division=%s, Phone_no=%s WHERE Student_ID=%s"
                my_cursor.execute(query, (
                      

                                                                                                                                      self.var_year.get(),
                                                                                                                                      self.var_semester.get(),
                                                                                                                                      self.var_gender.get(),
                                                                                                                                      self.var_program.get(),
                                                                                                                                      self.var_std_name.get(),
                                                                                                                                      self.var_div.get(),
                                                                                                                                      self.var_phone.get(),
                                                                                                                                      self.var_std_id.get() ==id+1
                                                                                                                                 
                                                                                                                                        ) )    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    


 
if __name__=="__main__":
    root=Tk()
    obj=StudentDetails(root)
    root.mainloop()
        







         

        




         


        









       




        
        

        
        














