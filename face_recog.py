from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import  cv2
 


 
class Face_Recog: 
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Security System")
        self.root.geometry("1751x790+0+0")

        # Load background image
        bg_img = Image.open(r"D:\D drive\Python\Images\13.JPG")
        bg_img = bg_img.resize((1751, 790), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        # Create a label to display the background image
        self.bg_label = Label(self.root, image=self.photoimg_bg)
        self.bg_label.pack()
        
        #Face Recognittion button
        img8 = Image.open(r"D:\D drive\Python\Images\training.JPG")
        img8 = img8.resize((300, 300), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button( self.root,image=self.photoimg8, cursor="hand2",command=self.Face_Recog)
        b1.place(x=470, y=300, width=300, height=280)

        b1_1=Button(self.root, text="Recognize Face",cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white",command=self.Face_Recog )
        b1_1.place(x=470,y=580,width=300,height=70)


        # cOVER IMAGE
        img1 = Image.open(r"D:\D drive\Python\Images\11.JPG")
        img1 = img1.resize((1751, 220), Image.LANCZOS)   
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1751, height=220)


    #Attendance button 
    def mark_attendance(self, i, r, n, m):
        with open("data.csv", "r+", newline="\n") as f:
             myDataList = f.readlines()
             name_list = []

        # Create a set of existing names for faster lookups
        for line in myDataList:
            entry = line.split(",")
            name_list.append(entry[0])

        if (i not in name_list):
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            attendance_data = f"{i},{n},{r},{m},{dtString},{d1},Present\n"

            # Append the attendance data to the file
            with open("data.csv", "a", newline="\n") as f:
                f.write(attendance_data)



    #face recognition

    def Face_Recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,face_recognizer):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=face_recognizer.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password= "20202023@ALI",database="myfyp")
                my_cursor=conn.cursor()

                my_cursor.execute("select Year from student where Student_ID="+str(id))
                m=my_cursor.fetchone()
                m= "+".join(m)

                my_cursor.execute("select Gender from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r= "+".join(r) 

                my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i= "+".join(i) 
 
                my_cursor.execute("select Student_Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n= "+".join(n)
           
                

                conn.close() 

 
                if confidence > 82:
                 cv2.putText(img, f"Year: {m}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Gender: {r}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Student_ID: {i}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Student_Name: {n}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 self.mark_attendance(i,r,n,m)
                else:
                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)


                coord=[x,y,w,h]

            return coord
        
        def recognize (img,face_recognizer,faceCascade):
            draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",face_recognizer)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        face_recognizer=cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize (img,face_recognizer,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

 
if __name__=="__main__":
    root=Tk()
    obj=Face_Recog(root)
    root.mainloop()        