from pytube import *
from tkinter import *
link = input('enter the video Link : ')


vd = YouTube(link)


vdL = vd.streams.filter(only_audio=True)

vdlP = list(enumerate(vdL))


for i in vdlP :
    print(i)
    
vdlI = int(input("Enter the Option : "))

vdL[vdlI].download()

print("downloading Complete")
    