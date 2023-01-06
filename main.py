from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

def getImage():
    l= instaloader.Instaloader()
    profile = instaloader.Profile.from_username(l.context, f'{username.get()}')
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image = pic

window = Tk()
window.geometry("600x600")
window.minsize(300, 300)
window.maxsize(800, 800)
window.title('Instagram profile downloader')

# input
username = Entry(window, width=50)
username.pack()

# button
button = Button(window, text='Start downloading', fg='white', bg='grey')
# button.place(x=240, y=30)
button.pack()
button.config(command=getImage)
label = Label(window)

window.mainloop()


