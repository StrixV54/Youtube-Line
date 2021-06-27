from tkinter import *
import pathlib
from vlc import Instance
import time
import pafy
import io
from pytube import YouTube
from tkinter import messagebox,filedialog
from youtubesearchpython import VideosSearch

class YoutubePLR:
    
    def __init__(self):
        self.Player = Instance('--loop')

    def Vplayer(self, url):
        url=str(url)
        video = pafy.new(url)
        best = video.getbest()
        """media = vlc.MediaPlayer(best.url)
        media.play()"""
        #player = vlc.Instance()
        self.media_list = self.Player.media_list_new()
        self.media_player = self.Player.media_list_player_new()
        self.media = self.Player.media_new(best.url)
        self.media_list.add_media(self.media)
        self.media_player.set_media_list(self.media_list)
        self.media_player.play()
        time.sleep(15)

    def stopVideo(self):
        #media.stop()
        print("Stoping")
        self.media_player.stop()
        #sys.exit()

    def callSearch(self):
        videoName=str(self.video_Name.get())
        print(videoName)
        if videoName is not None:
            videosSearch = VideosSearch(str(videoName), limit = 5)

            for i in range(5):
                self.titleList.append(str(videosSearch.result()['result'][i]['title'][0:45]))
                self.linkList.append(videosSearch.result()['result'][i]['link'])
            for i in range(5):
                print(self.titleList[i],"\t\t",self.linkList[i])
                #print(videosSearch.result()['result'][i]['title'][0:45])
            self.WidgetResult()
        else:
            print("Null Search")

    def Browse(self):
        download_Directory=filedialog.askdirectory(
            initialdir=pathlib.Path.cwd())
        self.download_Path.set(download_Directory)

    def Download(self):
        Youtube_link=str(self.linkList[0])
        print(Youtube_link)
        download_Folder=self.download_Path.get()
        getVideo=YouTube(Youtube_link)
        videoStream=getVideo.streams.first()
        videoStream.download(download_Folder)
        messagebox.showinfo("Successfully","Downloaded and Saved in\n"+download_Folder)

    def Widgets(self):
        link_label=Label(self.root, text="Youtube Search",bg="#E8D579",width=20)
        link_label.grid(row=1,column=0,pady=5,padx=5)

        linkText=Entry(self.root,width=40,textvariable=self.video_Name)
        linkText.insert(END, 'attention')
        linkText.grid(row=1,column=1,pady=5,padx=5)

        destination_label=Label(self.root, text="Destination",bg="#E8D579",width=20)
        destination_label.grid(row=2,column=0,pady=5,padx=5)

        destiText=Entry(self.root,width=40,textvariable=self.download_Path)
        destiText.grid(row=2,column=1,pady=5,padx=5) 

        browse_B=Button(self.root,text="Browse",command=self.Browse,width=15,bg="#05E8E0")
        browse_B.grid(row=2,column=2,pady=5,padx=5)
        print(self.video_Name.get())
        Search_B=Button(self.root,text="Search",command=self.callSearch,width=15,bg="#05E8E0")
        Search_B.grid(row=1,column=2,pady=5,padx=5)

    def WidgetResult(self):
        self.root.geometry("550x200")
        time.sleep(1)
        self.root.geometry("620x300")
        time.sleep(1)
        colrLab="#cccccc"
        colrBut="#fd9c35"
        #command= lambda: self.Vplayer(self.linkList[0])

        resultLabel_1=Label(self.root, text=self.titleList[0],bg=colrLab,width=50)      #1
        resultLabel_1.grid(row=3,columnspan=2,pady=5,padx=5)

        Search_B_1=Button(self.root,text="Play",command= lambda: self.Vplayer((self.linkList[0])),width=10,bg=colrBut)
        Search_B_1.grid(row=3,column=2,pady=1,padx=1)

        Download_B=Button(self.root,text="Download",command=self.Download,width=10,bg="#a2cf6e",bd=1)
        Download_B.grid(row=3,column=3,pady=3,padx=3)

        resultLabel_2=Label(self.root, text=self.titleList[1],bg=colrLab,width=50)      #2
        resultLabel_2.grid(row=4,columnspan=2,pady=5,padx=5)

        Search_B_2=Button(self.root,text="Play",command= lambda: self.Vplayer(self.linkList[1]),width=10,bg=colrBut)
        Search_B_2.grid(row=4,column=2,pady=1,padx=1)

        resultLabel_3=Label(self.root, text=self.titleList[2],bg=colrLab,width=50)      #3
        resultLabel_3.grid(row=5,columnspan=2,pady=5,padx=5)

        Search_B_3=Button(self.root,text="Play",command= lambda: self.Vplayer(self.linkList[2]),width=10,bg=colrBut)
        Search_B_3.grid(row=5,column=2,pady=1,padx=1)

        resultLabel_4=Label(self.root, text=self.titleList[3],bg=colrLab,width=50)      #4
        resultLabel_4.grid(row=6,columnspan=2,pady=5,padx=5)

        Search_B_4=Button(self.root,text="Play",command= lambda: self.Vplayer(self.linkList[3]),width=10,bg=colrBut)
        Search_B_4.grid(row=6,column=2,pady=1,padx=1)

        resultLabel_5=Label(self.root, text=self.titleList[4],bg=colrLab,width=50)      #5
        resultLabel_5.grid(row=7,columnspan=2,pady=5,padx=5)

        Search_B_5=Button(self.root,text="Play",command= lambda: self.Vplayer(self.linkList[4]),width=10,bg=colrBut)
        Search_B_5.grid(row=7,column=2,pady=1,padx=1)

        Stop_B=Button(self.root,text="Stop Video",command=self.stopVideo,width=20,bg="#a2cf6e")
        Stop_B.grid(row=8,column=1,pady=3,padx=3)

        #Download_B=Button(self.root,text="Download",command=Download,width=20,bg="#a2cf6e",bd=1)
        #Download_B.grid(row=9,column=1,pady=3,padx=3)

    def Start(self):
        self.root=Tk()
        self.root.geometry("550x110")
        #self.root.resizable(0,0)
        self.root.title("Youtube Video Downloader")
        self.root.config(background="#000000")
        self.video_Name=StringVar()
        self.download_Path=StringVar()
        self.titleList=[];
        self.linkList=[];

        self.Widgets()
        self.root.mainloop()  
        
player = YoutubePLR()
player.Start()