import tkinter as tk
#from PIL import Image, ImageTk
#from playsound import playsound

WINDOW_TITLE = "My Closet"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500
class ClosetApp: 
    def __init__(self, root):
        self.root = root
        self.create_bakground()

    def create_bakground(self): 
        
        #window title + name 
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))



root = tk.Tk()
app = ClosetApp(root)
root.mainloop()