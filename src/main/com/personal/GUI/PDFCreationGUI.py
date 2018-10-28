import Tkinter as tk
import tkFileDialog
from src.main.com.personal.conversions.ImagesToPDF import ImagesToPDF


directory = ""


def display_in_center(window, width=400, height=400, title="My App"):
    """
    
    :param window: 
    :param width: 
    :param height: 
    :param title: 
    :return: 
    """
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)

    # set the dimensions of the screen
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    window.title(title)

    return window


def add_label(text='Sample Label', column=0, row=0):
    tk.Label(text=text).grid(column=column, row=row)


def add_button(text="Sample Button", column=0, row=0):
        tk.Button(text=text).grid(column=column, row=row)


def browse():
    print "im called"
    curr_dir = tkFileDialog.askdirectory()
    msg = ImagesToPDF().convertToPDF(curr_dir)
    print 'msg --> ', msg


def main():
    window = tk.Tk()
    window = display_in_center(window=window, title="Image To PDF Converter")
    add_label(text="Select Location of Images : ", column=0, row=0)
    tk.Button(text='Browse', command=browse())

    window.mainloop()


main()
