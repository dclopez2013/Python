
from tkinter import *


root = Tk()
root.title("YouTube Audio/Video Assistant")
root.minsize(width=600,height=400)


#vars
int = IntVar()

#labels
lbl = Label(root, text="Enter URL here", font=20,width=25)

streamLbl = Label(root, text="Video Description", font=20,pady=30,anchor=CENTER)
rightLbl = Label(root, text="*************", font=20,pady=30,anchor=E)

#buttons and inputs
audioR = Radiobutton(root,text="Download Audio Only", variable=int, value=1)
videoR = Radiobutton(root,text="Download Full Video", variable=int, value=2 )
btn = Button(root, text="Download",pady=10,padx=20)
urlE = Entry(root, width=50)

Ipath="pythonImg.png"
imgLoad = PhotoImage(file="pythonImg.png")
imgLabel = Label(root, image=imgLoad)
creditLabel = Label(root,text="Brought To you by Python Programming Languge")
lbl.grid(row=0)
urlE.grid(row=0, column=1)
streamLbl.grid(row=1,column=1)
rightLbl.grid(row=1,column=0)
audioR.grid(row=2)
videoR.grid(row=2,column=1)
creditLabel.grid(row=4)
btn.grid(row=3,column=1)
imgLabel.grid(row=3,column=0)
root.mainloop()