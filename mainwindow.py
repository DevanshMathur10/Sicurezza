from tkinter import *
from location import locshow
from tkvideo import tkvideo
from emailsender import sendpass
import time

def mainwin(name):

    root1=Toplevel()
    root1.title("SICUREZZA")
    root1.geometry("1920x1080")
    root1.state('zoomed')

    imglbl=Label(root1)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)
    player = tkvideo("C:/Users/dr_de/Documents/VS/testnew.mp4", imglbl,loop = 1, size = (1920,1080))
    player.play()

    frame1=Frame(root1,bg='#2E0063', relief=RAISED)
    frame1.place(x=760,y=185,anchor='center')

    sendbtn=Button(frame1,text="SHOW\nUSER'S\nLOCATION",command=locshow)
    sendbtn.grid(row=1,column=1,columnspan=2,ipady=30,ipadx=50)

    frame2=Frame(root1,bg='#2E0063', relief=RAISED)
    frame2.place(x=760,y=300,anchor='center')

    sendbtn=Button(frame2,text="SEND\nSOS",command=sendpass(name))
    sendbtn.grid(row=2,column=1,columnspan=2,ipady=30,ipadx=70)

    frame2=Frame(root1,highlightbackground="#000000", highlightthickness=1.5)
    frame2.place(x=760,y=75,anchor='center')

    labelt = Label(frame2, font=("Boulder", 25, 'bold'), bg="#1e2114", fg="#fff708", bd=25) 
    labelt.grid(row=0, column=0)

    def digital_clock(): 
            time_live = time.strftime("%I:%M:%S %p")
            labelt.config(text=time_live) 
            labelt.after(200, digital_clock)
    digital_clock()

    root1.mainloop()
