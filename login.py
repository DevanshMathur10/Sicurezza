from tkinter import *
from tkvideo import tkvideo
from mainwindow import mainwin
import pandas as pd

filename="data.csv"
df = pd.read_csv(filename)
root=Tk()
root.title("LOGIN")
root.geometry("845x710")
root.configure(bg='#232754')
root.state('zoomed')

imglbl=Label(root)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)
player = tkvideo("C:/Users/dr_de/OneDrive/Documents/VS/INSPIRONTREK/loginback.mp4", imglbl,loop = 1, size = (1920,1080))
player.play()

frame=Frame(root,bg='#232754', relief=RAISED)
frame.place(x=760,y=390,anchor='center')

NAME=Label(frame,text="Name",background="#232754",fg='white', font=('Book Antiqua', 11))
NAME.grid(row=0,column=0,padx=8,pady=(5,0))
password=Label(frame,text="Pass",background="#232754",fg='white', font=('Book Antiqua', 11))
password.grid(row=2,column=0)
ec1=Label(frame,text="EC1",background="#232754",fg='white', font=('Book Antiqua', 11))
ec1.grid(row=3,column=0)
ec2=Label(frame,text="EC2",background="#232754",fg='white', font=('Book Antiqua', 11))
ec2.grid(row=4,column=0)

NAME_box=Entry(frame,width=35,borderwidth=2)
NAME_box.grid(row=0,column=1,pady=(5,0),padx=10)
pass_box=Entry(frame,width=35,borderwidth=2)
pass_box.grid(row=2,column=1)
ec1_box=Entry(frame,width=35,borderwidth=2)
ec1_box.grid(row=3,column=1)
ec2_box=Entry(frame,width=35,borderwidth=2)
ec2_box.grid(row=4,column=1)

def submitpass():
    if NAME_box.get().strip() in df["name"].values:
        passshow=Label(frame,text=" USER SIGNED IN ",background="#232754",fg='white', font=('arial', 9))
        passshow.grid(row=6,column=0,columnspan=2,padx=8)
        mainwin()
    else:
        nd=pd.DataFrame([[NAME_box.get(),pass_box.get(),ec1_box.get(),ec2_box.get()]],columns=['name','pass','ec1','ec2'])
        nd.to_csv('data.csv', mode='a', index=False, header=False)
        passshow=Label(frame,text=" USER SIGNED IN ",background="#232754",fg='white', font=('arial', 9))
        passshow.grid(row=6,column=0,columnspan=2,padx=8)
        mainwin()
checkbtn=Button(frame,text="SIGN IN",command=submitpass)
checkbtn.grid(row=5,column=1,columnspan=2,padx=10,pady=5,ipadx=45)

root.mainloop()