from tkinter import *
import pathlib
import vlc
import time
import pafy
import io
from pytube import YouTube
from tkinter import messagebox,filedialog
from youtubesearchpython import VideosSearch

root=Tk()
root.geometry("550x110")
#root.resizable(0,0)
root.title("Youtube Video Downloader")
root.config(background="#000000")
video_Name=StringVar()
download_Path=StringVar()
titleList=[];
linkList=[];

def Vplayer(url):
    url=str(url)
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
    time.sleep(10)

def stopVideo():
    media.stop()

def callSearch():
    if video_Name.get() is not None:
        videosSearch = VideosSearch(str(video_Name.get()), limit = 5)

        for i in range(5):
            titleList.append(str(videosSearch.result()['result'][i]['title'][0:45]))
            linkList.append(videosSearch.result()['result'][i]['link'])
        for i in range(5):
            print(titleList[i])
            #print(videosSearch.result()['result'][i]['title'][0:45])
        WidgetResult()
    else:
        print("Null")

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

    linkText=Entry(root,width=40,textvariable=video_Name)
    linkText.grid(row=1,column=1,pady=5,padx=5)

    destination_label=Label(root, text="Destination",bg="#E8D579",width=20)
    destination_label.grid(row=2,column=0,pady=5,padx=5)

    destiText=Entry(root,width=40,textvariable=download_Path)
    destiText.grid(row=2,column=1,pady=5,padx=5) 

    browse_B=Button(root,text="Browse",command=Browse,width=15,bg="#05E8E0")
    browse_B.grid(row=2,column=2,pady=5,padx=5)

    Search_B=Button(root,text="Search",command=callSearch,width=15,bg="#05E8E0")
    Search_B.grid(row=1,column=2,pady=5,padx=5)

def WidgetResult():
    root.geometry("550x300")
    colrLab="#cccccc"
    colrBut="#fd9c35"
    #command=Vplayer(linkList[0])

    resultLabel_1=Label(root, text=titleList[0],bg=colrLab,width=50)      #1
    resultLabel_1.grid(row=3,columnspan=2,pady=5,padx=5)

    Search_B_1=Button(root,text="Play",command=Vplayer(linkList[0]),width=10,bg=colrBut)
    Search_B_1.grid(row=3,column=2,pady=1,padx=1)

    resultLabel_2=Label(root, text=titleList[1],bg=colrLab,width=50)      #2
    resultLabel_2.grid(row=4,columnspan=2,pady=5,padx=5)

    Search_B_2=Button(root,text="Play",command=Vplayer(linkList[1]),width=10,bg=colrBut)
    Search_B_2.grid(row=4,column=2,pady=1,padx=1)

    resultLabel_3=Label(root, text=titleList[2],bg=colrLab,width=50)      #3
    resultLabel_3.grid(row=5,columnspan=2,pady=5,padx=5)

    Search_B_3=Button(root,text="Play",width=10,bg=colrBut)
    Search_B_3.grid(row=5,column=2,pady=1,padx=1)

    resultLabel_4=Label(root, text=titleList[3],bg=colrLab,width=50)      #4
    resultLabel_4.grid(row=6,columnspan=2,pady=5,padx=5)

    Search_B_4=Button(root,text="Play",width=10,bg=colrBut)
    Search_B_4.grid(row=6,column=2,pady=1,padx=1)

    resultLabel_5=Label(root, text=titleList[4],bg=colrLab,width=50)      #5
    resultLabel_5.grid(row=7,columnspan=2,pady=5,padx=5)

    Search_B_5=Button(root,text="Play",width=10,bg=colrBut)
    Search_B_5.grid(row=7,column=2,pady=1,padx=1)

    Stop_B=Button(root,text="Stop Video",width=20,bg="#a2cf6e",bd=1)
    Stop_B.grid(row=8,column=1,pady=3,padx=3)

    #Download_B=Button(root,text="Download",command=Download,width=20,bg="#a2cf6e",bd=1)
    #Download_B.grid(row=9,column=1,pady=3,padx=3)

Widgets()
root.mainloop()  