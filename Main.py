from tkinter import *
import pathlib
from pytube import YouTube

root=Tk()
root.geometry("500x110")
root.resizable(0.0)
root.title("Youtube Video Downloader")
root.config(background="#000000")
video_Link=StringVar()
download_Path=StringVar()
Widgets()
root.mainloop()    

def Download():
    Youtube_Link=video_Link.get()
    download_Folder=Download_Path.get()
    getVideo=YouTube(Youtube_Link)
    videoStream=getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("Successfully","Downloaded and Saved in\n"+download_Folder)

def Browse():
    download_Directory=filedialog.askdirectory(
        initialdir=pathlib.Path.cwd())
    download_Path.set(download_Directory)



