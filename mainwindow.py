from tkinter import *
from location import locshow
from tkvideo import tkvideo

def mainwin():

    root1=Toplevel()
    root1.title("SAFE")
    root1.geometry("1920x1080")
    root1.state('zoomed')

    imglbl=Label(root1)
    imglbl.place(x=0, y=0, relwidth=1, relheight=1)
    player = tkvideo("C:/Users/dr_de/Documents/VS/testnew.mp4", imglbl,loop = 1, size = (1920,1080))
    player.play()

    frame1=Frame(root1,bg='#2E0063', relief=RAISED)
    frame1.place(x=550,y=75,anchor='center')

    sendbtn=Button(frame1,text="SHOW\nUSER'S\nLOCATION",command=locshow)
    sendbtn.grid(row=1,column=1,columnspan=2,ipady=30,ipadx=50)

    

    root1.mainloop()
    

