from tkinter import *
import pathlib
from pytube import YouTube
from tkinter import messagebox,filedialog

root=Tk()
root.geometry("500x110")
root.resizable(0,0)
root.title("Youtube Video Downloader")
root.config(background="#000000")
video_Link=StringVar()
download_Path=StringVar()

def Browse():
    download_Directory=filedialog.askdirectory(
        initialdir=pathlib.Path.cwd())
    download_Path.set(download_Directory)

def Download():
    Youtube_Link=video_Link.get()
    download_Folder=download_Path.get()
    getVideo=YouTube(Youtube_Link)
    videoStream=getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("Successfully","Downloaded and Saved in\n"+download_Folder)

def Widgets():
    link_label=Label(root, text="Youtube link",bg="#E8D579",width=20)
    link_label.grid(row=1,column=0,pady=5,padx=5)

    linkText=Entry(root,width=55,textvariable=video_Link)
    linkText.grid(row=1,column=1,pady=5,padx=5,columnspan=2)

    destination_label=Label(root, text="Destination",bg="#E8D579",width=20)
    destination_label.grid(row=2,column=0,pady=5,padx=5)

    linkText=Entry(root,width=40,textvariable=download_Path)
    linkText.grid(row=2,column=1,pady=5,padx=5) 

    browse_B=Button(root,text="Browse",command=Browse,width=10,bg="#05E8E0")
    browse_B.grid(row=2,column=2,pady=1,padx=1)

    Download_B=Button(root,text="Download",command=Download,width=20,bg="#05E8E0")
    Download_B.grid(row=3,column=1,pady=3,padx=3)

Widgets()
root.mainloop()  