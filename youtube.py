import tkinter as tk
import os
import youtube_dl
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

# Creating a window
root = tk.Tk()
# For changing the icon of the title bar
root.iconbitmap(r'image.ico')
# For changing the title of the title bar
root.title('Video Downloader')
# To set the dimensions of the window
root.geometry('400x400')
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE,height=FALSE)
# Creating a canvas
canvas1 = tk.Canvas(root,height = 400,width = 400,bg = "pink")
# Attaching the canvas
canvas1.pack()
# Set the family,size and style of the font
bold_font = tkfont.Font(family = "calibre", size = 12,weight = "bold")
# Creating a label with a text and attaching it to the root
label1 = tk.Label(root,text = "Enter the URL",width = 10,bg = "pink")
# adding the font features to the label
label1.config(font = bold_font)
# placing the label in the canvas
canvas1.create_window(200,140,window = label1)
# Text Area
download_entry = tk.Entry(root)
canvas1.create_window(200,180,window = download_entry)
def get_video_url():
# Get the user entered URL
  search_item = download_entry.get()
# To specify the format of video, whether it's a playlist, whether to extract the audio or not
  ydl_opts = {'format': 'best','noplaylist':True,'extract-  audio':True,}
# Destination Path where we save the downloaded file
  os.chdir('H:\you tube')
# downloading the file
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([search_item])
# Set the family,size and style of the font
bold_font2 = tkfont.Font(family="calibre", size=10, weight="bold")
#Button widget is used in which we enter the name of the button, the padding,the text color,the background color of the button,command to be performed when clicked.
download = tk.Button(text= "Download", padx=5,pady=5,fg = "white",bg = "DeepSkyBlue4",command = get_video_url)
# Attaching to the canvas
canvas1.create_window(200,230,window=download)
root.mainloop()
