from tkinter import *
from tkinter import messagebox
import pytube
import threading


#variabkles


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        global audioR
        global videoR
        global urlE
        global intChoice
        global downloads
        global statusDone
        self.master.title("YouTube Audio/Video Assistant")
        self.pack(fill=BOTH, expand=1)
        intChoice = IntVar()
        intChoice.set(1)
        btn = Button(self, text="Download",font =20, command=self.FullDownload)
        btn2 = Button(self, text="Clear", font=20, command=self.clear)
        lbl = Label(self, text="Enter Your YouTube URL here",font =20)
        streamLbl = Label(self, text="Video Description",font =20)
        fillerLbl = Label(self, text="**************************************************************************************",font =20)
        audioR = Radiobutton(self, text="Download Audio Only", variable=intChoice, value=1)
        videoR = Radiobutton(self, text="Download Full Video", variable=intChoice, value=2)
        urlE = Entry(self,  width=50)
        #image = PhotoImage(file='pythonImgGif.gif')
       # imgLabel=Label(image=image)
        #imgLabel.image = image
        creditLabel = Label(self, text="Brought To you by Python Programming Languge",font =20)
        downLabel = Label(self, text="Chose whether you want just the audio or the whole video", font=20)
        downloads= Text(self,height=8,width=55,borderwidth=2,relief="solid")
        currentLabel = Label(self,text="Your Current Downloads")
        status = Label(self, text= "Curret Download Statuses:")
        statusDone = Label(self, text="NA")
        #placement
        lbl.place(x=75,y=50)
        urlE.place(x=400,y=50)
        fillerLbl.place(x=100,y=100)
        downLabel.place(x=200,y=130)
        audioR.place(x=200,y=175)
        videoR.place(x=400, y=175)
        creditLabel.place(x=50,y=250)
       # imgLabel.place(x=20,y=330)
        btn.place(x= 550,y=250)
        btn2.place(x=650, y=250)
        status.place(x=450,y=300)
        statusDone.place(x=650,y=300)
        downloads.place(x=450,y=330)

    def download(self):
        global urlchoice
        urlchoice= urlE.get()
        choice = intChoice.get()
        if not urlchoice:
            messagebox.showerror("Invalid Link","please ensure you copy the complete working youtube link from the browswer")
        else:
            try:
                    if (choice == 1):
                        youtube2 = pytube.YouTube(urlchoice)
                        song2 = youtube2.streams.filter(only_audio=True).first()
                        # downloads.insert(END, "\n" + youtube.title)
                        # statusDone.config(text="Downloading")
                        song2.download()
                    if(choice == 2):
                        youtube = pytube.YouTube(urlchoice)
                        song = youtube.streams.first()
                        #downloads.insert(END,"\n"+youtube.title)
                       # statusDone.config(text="Downloading")
                        print(song)
                        song.download()
            except Exception as ex:
                messagebox.showerror("Invalid Link",ex)
                self.clear()


    def clear(self):
        urlE.delete(0,END)


    def FullDownload(self):
         self.download()

root = Tk()
root.geometry("900x500")
app = Window(root)

root.mainloop()
