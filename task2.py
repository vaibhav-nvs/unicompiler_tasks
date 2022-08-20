from tkinter import *
#from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

root=Tk()
root.title('Music player project by Ramprasad')
root.geometry("920x670+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(False, False)
mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#icon
Icon_Image = PhotoImage(file="icon.png")
root.iconphoto(False,Icon_Image)
 
#Top_Image = PhotoImage(file="top.png")
#Label(root, image=Top_Image, bg="#0f1a2b").pack()
 
#logo
logo_Image = PhotoImage(file="logo.png")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=50, y=115)

# Button
Button_Play = PhotoImage(file="play.png")
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=100, y=30)
 
Button_Stop = PhotoImage(file="stop.png")
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=300, y=30)
 
Button_Resume = PhotoImage(file="resume.png")
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=500, y=30)
 
Button_Pause = PhotoImage(file="pause.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=700, y=30)
 
#music
#Menu = PhotoImage(file="menu.png")
#Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)
 
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=575, y=450, width=340, height=200)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=575, y=395)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()
