from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import  cv2
import os
import numpy as np

 
class trainDetails:
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
        
        #Train Data button
        img8 = Image.open(r"D:\D drive\Python\Images\training.JPG")
        img8 = img8.resize((300, 300), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button( self.root,image=self.photoimg8, cursor="hand2")
        b1.place(x=470, y=300, width=300, height=280)

        b1_1=Button(self.root, text="Train Data",cursor="hand2",font=("archivo black",15,"bold"),bg="darkblue",fg="white",command=self.train_classifier)
        b1_1.place(x=470,y=580,width=300,height=70)

        # cOVER IMAGE
        img1 = Image.open(r"D:\D drive\Python\Images\11.JPG")
        img1 = img1.resize((1751, 220), Image.LANCZOS)   
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1751, height=220)

        


        


    def train_classifier(self):   
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save
        face_recognizer =cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.train(faces, ids)
        face_recognizer.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


if __name__=="__main__":
    root=Tk()
    obj=trainDetails(root)
    root.mainloop()
