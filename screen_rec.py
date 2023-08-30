from tkinter import *
import pyscreenrec
from mss import mss

root=Tk()
root.geometry("400x700")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),2)
    my_label.config(text="Recording Started!")

def pause_rec():
    rec.pause_recording()
    my_label.config(text="Recording Paused!")

def resume_rec():
    rec.resume_recording()
    my_label.config(text="Recording Resumed!")

def stop_rec():
    rec.stop_recording()
    my_label.config(text="Recording Stoped!")

def ss_capture():
    my_label.config(text="Screen Shot Has Been Saved!")
    with mss() as sct:
	    Filename = sct.shot(mon=1, output="output.png")	
        
rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="img\icon.png")
root.iconphoto(False,image_icon)

#background image 
image1=PhotoImage(file="img\yelllow.png")
Label(root,image=image1,bg="#fff").place(x=-2,y=35)

image2=PhotoImage(file="img\\blue.png")
Label(root,image=image2,bg="#fff").place(x=223,y=200)

#heading 
lbl=Label(root,text="Screen Recorder",bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

image3=PhotoImage(file="img\\recording.png")
Label(root,image=image3,bd=0).pack(pady=30)

#file Name
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=10,font="arial 15")
entry.place(x=100,y=350)
Filename.set("Type Name")

#buttons 
start=Button(root,text="Start",font="arial 15",bd=0,command=start_rec)
start.place(x=140,y=260)

image4=PhotoImage(file="img\pause.png")
pause=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450)

image5=PhotoImage(file="img\\resume.png")
resume=Button(root,image=image5,bd=0,bg="#fff",command=resume_rec)
resume.place(x=150,y=450)

image6=PhotoImage(file="img\stop.png")
stop=Button(root,image=image6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450)

image7=PhotoImage(file="img\ss.png")
ss=Button(root,image=image7,bd=0,bg="#fff",command=ss_capture)
ss.place(x=150,y=550)

#about
my_label = Label(root, text="")
my_label.place(x=70,y=640)

root.mainloop()