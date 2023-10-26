from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import StudentDetails
import os
from tkinter import Tk, Button, Toplevel
from train import trainDetails
from face_recog import Face_Recog
from Attendance import AttendanceDetails
 

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Security System")
        self.root.geometry("1751x790+0+0")

        # COVER IMAGE
        img1 = Image.open(r"D:\D drive\Python\Images\11.JPG")
        img1 = img1.resize((1751, 220), Image.LANCZOS)   
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1751, height=220)

         

        #Background_Image
        img4 = Image.open(r"D:\D drive\Python\Images\13.JPG")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=210, width=1530, height=710)

        #Student_Button
        img5=Image.open(r"D:\D drive\Python\Images\14.JPG")
        img5=img5.resize((170,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=30,y=100,width=170,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=30,y=300,width=170,height=40)

        
        #Detect_Face_Button
        img6=Image.open(r"D:\D drive\Python\Images\15.JPG")
        img6=img6.resize((170,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_detector)
        b1.place(x=235,y=100,width=170,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white",)
        b1_1.place(x=235,y=300,width=170,height=40)

        #Attendance_Button
        img7=Image.open(r"D:\D drive\Python\Images\16.JPG")
        img7=img7.resize((170,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=440,y=100,width=170,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=440,y=300,width=170,height=40)



        #Train Data button
        img8 = Image.open(r"D:\D drive\Python\Images\18.JPG")
        img8 = img8.resize((170, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=645, y=100, width=170, height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white",command=self.train_data)
        b1_1.place(x=645,y=300,width=170,height=40)


        #Photos button
        img9 = Image.open(r"D:\D drive\Python\Images\19.JPG")
        img9 = img9.resize((170, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=850, y=100, width=170, height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("archivo black",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=300,width=170,height=40)
 

        # Exit button
        img11 = Image.open(r"D:\D drive\Python\Images\20.JPG")
        img11 = img11.resize((170, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.exit)
        b1.place(x=1055, y=100, width=170, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("archivo black", 15, "bold"), bg="darkblue", fg="white", command=self.exit)
        b1_1.place(x=1055, y=300, width=170, height=40)

    #open image
    def open_img(self):
        os.startfile("data")


    # Function Button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentDetails(self.new_window)
    
    # Train Data Button
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = trainDetails(self.new_window)


    # Face Detector Button
    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recog(self.new_window)    

    # Attendance Button
    def attendance_data(self):    
        self.new_window = Toplevel(self.root)
        self.app = AttendanceDetails(self.new_window) 


     #exit button
    def exit(self):   
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
