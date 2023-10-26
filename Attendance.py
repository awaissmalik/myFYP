from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata=[]
class AttendanceDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Security System")
        self.root.geometry("1751x790+0+0")
        
        #variables

        self.var_atten_id=StringVar()
        self.var_atten_year=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_gender=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


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
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendandce Details",font=("archivo black",12,"bold"))
        Left_frame.place(x=0,y=10,width=660,height=500)

        img_left=Image.open(r"D:\D drive\Python\Images\12.JPG")
        img_left=img_left.resize((660,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=100)

        #Attendance_Frame
        attendance_frame=LabelFrame(Left_frame)
        attendance_frame.place(x=5,y=110,width=650,height=300)

        #studentID_button
        studentID_label=Label( attendance_frame, text="Student ID:",font=("archivo black",10),bg="white")
        studentID_label.grid(row=1,column=0,padx=10,sticky=W)

        studentName_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_id, width=15,font=("archivo black",10))
        studentName_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Student_Name
        studentName_label=Label(attendance_frame,  text="Student Name:",font=("archivo black",10),bg="white")
        studentName_label.grid(row=1,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(attendance_frame ,textvariable=self.var_atten_name,width=15,font=("archivo black",10))
        studentName_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        #Year
        Year_label=Label(attendance_frame,text="Year:",font=("archivo black",10),bg="white")
        Year_label.grid(row=3,column=0,padx=10,sticky=W)

        Year_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_year, width=15,font=("archivo black",10))
        Year_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(attendance_frame,text="Gender:",font=("archivo black",10),bg="white")
        Gender_label.grid(row=3,column=2,padx=10,sticky=W)

        Gender_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_gender,width=15,font=("archivo black",10))
        Gender_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Time
        Time_label=Label(attendance_frame,text="Time:",font=("archivo black",10),bg="white")
        Time_label.grid(row=4,column=0,padx=10,sticky=W)

        Time_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_time,width=15,font=("archivo black",10))
        Time_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Date
        Date_label=Label(attendance_frame,text="Date:",font=("archivo black",10),bg="white")
        Date_label.grid(row=4,column=2,padx=10,sticky=W)

        Date_entry=ttk.Entry(attendance_frame,textvariable=self.var_atten_date,width=15,font=("archivo black",10))
        Date_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Attendance_Status
        attendance_label=Label(attendance_frame,text="Status",font=("archivo black",10),bg="white")
        attendance_label.grid(row=5,column=0,padx=0,sticky=W)

        attendance_combo=ttk.Combobox(attendance_frame,textvariable=self.var_atten_attendance, font=("archivo black",10),state="readonly",width=17)
        attendance_combo["values"]=("Status","Present","Absent" )
        attendance_combo.current(0)
        attendance_combo.grid(row=5,column=1,padx=12,pady=10,sticky=W)

        #button_frame
        button_frame=Frame(attendance_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=140,width=650,height=50)

        #Import_button
        save_button=Button(button_frame,text="Import CSV",command=self.import_csv,width=19,font=("archivo black",10),bg="blue",fg="white" )

        save_button.grid(row=0,column=0)

        #Export_button
        update_button=Button(button_frame,text="Export CSV", command=self.export_csv, width=19,font=("archivo black",10),bg="blue",fg="white" )
        update_button.grid(row=0,column=1)

        #Delete_button
        delete_button=Button(button_frame,text="Delete",width=19,font=("archivo black",10),bg="blue",fg="white",command=self.delete )
        delete_button.grid(row=0,column=2)

        #Reset_button
        reset_button=Button(button_frame,text="Reset",width=19,font=("archivo black",10),bg="blue",fg="white" ,command=self.reset )
        reset_button.grid(row=0,column=3)

        #Right_frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("archivo black",12,"bold"))
        Right_frame.place(x=680,y=10,width=590,height=450)

        img_right=Image.open(r"D:\D drive\Python\Images\17.JPG")
        img_right=img_right.resize((660,100),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=100)

        
        #scroll bar table
        scroll_x=ttk.Scrollbar(Right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Right_frame,orient=VERTICAL)

        self.AttendanceReport_table=ttk.Treeview(Right_frame,column=("studentID","studentName","year","gender","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReport_table.xview)
        scroll_y.config(command=self.AttendanceReport_table.yview)

        
        self.AttendanceReport_table.heading("studentID",text="Student ID")
        self.AttendanceReport_table.heading("studentName",text="Student Name")
        self.AttendanceReport_table.heading("year",text="Year")
        self.AttendanceReport_table.heading("gender",text="Gender")
        self.AttendanceReport_table.heading("time",text="Time")
        self.AttendanceReport_table.heading("date",text="Date")
        self.AttendanceReport_table.heading("attendance",text="Attendance")

        self.AttendanceReport_table["show"]="headings"
         

        self.AttendanceReport_table.column("studentID",width=100)
        self.AttendanceReport_table.column("studentName",width=100)
        self.AttendanceReport_table.column("year",width=100)
        self.AttendanceReport_table.column("gender",width=100)
        self.AttendanceReport_table.column("time",width=100)
        self.AttendanceReport_table.column("date",width=100)
        self.AttendanceReport_table.column("attendance",width=100)
        
        self.AttendanceReport_table.pack(fill=BOTH,expand=1)
        self.AttendanceReport_table.bind("<ButtonRelease>", self.get_cursor)



    #=================fetch data======================
    def fetch_data(self,rows):
        self.AttendanceReport_table.delete(*self.AttendanceReport_table.get_children())
        for i in rows:
            self.AttendanceReport_table.insert("",END,values=i)

    #=================import csv======================
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #=================export csv======================
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


   



    #=================get cursor======================
    def get_cursor(self,event=""):
        cursor_focus=self.AttendanceReport_table.focus()
        content=self.AttendanceReport_table.item(cursor_focus)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_year.set(rows[2])
        self.var_atten_gender.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


     #=================reset======================
    def reset(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_year.set("")
        self.var_atten_gender.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
    def delete(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_year.set("")
        self.var_atten_gender.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
         
 

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceDetails(root)
    root.mainloop()        