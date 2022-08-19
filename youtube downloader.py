from tkinter import * #Tkinter is a standard GUI library helps to build a GUI application.
from pytube import YouTube #pytube is a library used to download youtube videos
def Downloader():     
    url =YouTube(str(web_link.get()))
	#Url variable gets the youtube link from the link variable by get() function and then str() will convert
	# the link in string datatype.
    print(url.streams)
    video = url.streams.get_highest_resolution()#This will let us download the higest resolution available
    video.download("D:\\") #This will download the video in the given path
    Label(base, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) #This is the acknowledgement given to the user
	#after downloading the video
base = Tk() #intializing a window
base.title("Youtube video downloader")
#after creating window for giving spcecifications we use geomentry,resizable
base.geometry('500x300')
base.resizable(0,0)
Label(base,text = 'Youtube Video Downloader', font ='arial 22 bold').pack()
#we need a string variable to store the url
web_link = StringVar()
Label(base, text = 'Paste video link Here:', font = 'arial 17 bold').place(x= 160 , y = 30)
web_link_enter = Entry(base, width = 70,textvariable = web_link).place(x = 32, y = 90) 
#on clicking the button Downloader fuction is called
Button(base,text = 'DOWNLOAD', font = 'arial 16 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
base.mainloop()#This will maintain the window until we close it