from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# total size container
file_size = 0

#this function called for updaing percentage...
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    try:
        #gets the percentage of the file that has been downloaded..
        file_downloaded = (file_size-remaining)
        per = (file_downloaded / file_size) * 100
        dBtn.config(text="{:00.0f} % Downloaded".format(per))
    except Exception as e:
        print(e)
        print("Error got when downloading video")

def startDownload():
    global file_size

    try:
        
        url = urlField.get()
        print(url)
        #changing button text
        dBtn.config(text='Please Wait......')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        ob = YouTube(url,on_complete_callback=progress)

        # strms = ob.streams.all()
        # for x in strms:
        #     print(x)

        strm = ob.streams.get_highest_resolution()
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(file_size)
        strm.download(path_to_save_video)
        print("Done")
        dBtn.config(text='Start Downloading')
        dBtn.config(state=NORMAL)
        showinfo("Downloaded Finished","Downloaded Successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()
    except Exception as e:
        print(e)
        print("Error got when downloading video")

def startDownloadThread():
    #creat thread
    thread = Thread(target=startDownload)
    thread.start()

#starting GUI  
main = Tk()

#setting title
main.title("My Youtube Downloader")

#set the icon
main.iconbitmap('C:\\Users\\alikh\\Desktop\\My_python\\icon.ico')
main.geometry("500x600")
#heading icon
file = PhotoImage(file='C:\\Users\\alikh\\Desktop\\My_python\\youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

#url textfield
urlField = Entry(main)
urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)
#download button
dBtn = Button(main,text="Start Download",font=("verdana",18),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)
vTitle = Label(main,text="Video Title")

main.mainloop()