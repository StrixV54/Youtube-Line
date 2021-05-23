from tkinter import *
import pathlib
import vlc
import time
import pafy
from pytube import YouTube
from tkinter import messagebox,filedialog

root=Tk()
root.geometry("500x110")
root.resizable(0,0)
root.title("Youtube Video Downloader")
root.config(background="#000000")
video_Link=StringVar()
download_Path=StringVar()

def Vplayer(url):
    url = "https://www.youtube.com/watch?v=nfs8NYg7yQM"
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
    print("Hello2")
    time.sleep(10) 

def Browse():
    download_Directory=filedialog.askdirectory(
        initialdir=pathlib.Path.cwd())
    download_Path.set(download_Directory)

def Download():
    Youtube_link=video_Link.get()
    download_Folder=download_Path.get()
    getVideo=YouTube(Youtube_link)
    videoStream=getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("Successfully","Downloaded and Saved in\n"+download_Folder)

def Widgets():
    link_label=Label(root, text="Youtube Search",bg="#E8D579",width=20)
    link_label.grid(row=1,column=0,pady=5,padx=5)

    linkText=Entry(root,width=40,textvariable=video_Link)
    linkText.grid(row=1,column=1,pady=5,padx=5)

    destination_label=Label(root, text="Destination",bg="#E8D579",width=20)
    destination_label.grid(row=2,column=0,pady=5,padx=5)

    destiText=Entry(root,width=40,textvariable=download_Path)
    destiText.grid(row=2,column=1,pady=5,padx=5) 

    browse_B=Button(root,text="Browse",command=Browse,width=10,bg="#05E8E0")
    browse_B.grid(row=2,column=2,pady=1,padx=1)

    Search_B=Button(root,text="Search",width=10,bg="#05E8E0")
    Search_B.grid(row=1,column=2,pady=1,padx=1)

    Download_B=Button(root,text="Download",command=Download,width=20,bg="#05E8E0")
    Download_B.grid(row=3,column=1,pady=3,padx=3)

Widgets()
root.mainloop()  