from tkinter import *
from tkinter import ttk
import time


def main_window():
    splash_root.destroy()
    root = Tk()
    root.title('BYDDP Notes')
    root.geometry('600x400')


#generates a 300x200 loading screen
splash_root = Tk()
splash_root.title('Loading Screen...')
splash_root.geometry('300x200')
splash_root.overrideredirect(True)
splash_label = Label(splash_root, text="Loading...",
                     font=('Helvetica', 20))
splash_label.pack(pady=20)


# opens loading screen for 3 seconds then opens the main app
splash_root.after(3000, main_window)
