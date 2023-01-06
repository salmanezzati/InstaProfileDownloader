from tkinter import *

window = Tk()
window.geometry("600x600")
window.minsize(300, 300)
window.maxsize(800, 800)
window.title('Instagram profile downloader')

# label
label = Label(window, text='Hallo Deutschland')
label.pack()

# button
def hello():
    # print(input.get())
    button.config(text=input.get())

button = Button(window, text='Suche starten', fg='white', bg='grey',command=hello)
# button.place(x=240, y=30)
button.pack()

# input
input = Entry(window)
input.pack()

window.mainloop()
