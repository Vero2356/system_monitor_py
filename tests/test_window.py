from tkinter import *

window = Tk() #instantiate an instance of window
Icon = PhotoImage(file='icon.png')
window.geometry("420x420")
window.title("Hardware statistics")
window.iconphoto(True, Icon)
window.config(background="#E8ECEF")
window.mainloop() # place window on screen and listens for events
print("hello")