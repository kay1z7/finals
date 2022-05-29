from logging import root
from tkinter import *

from PIL import Image, ImageTk, ImageDraw, ImageFont

root = Tk()
root.title('Batch image')
root.resizable(False, False)
root.iconbitmap("logo.ico")

my_img = ImageTk.PhotoImage(Image.open('photo5.png'))
my_label = Label(image=my_img)
my_label.pack(side=RIGHT)
    
def bw():
    img=Image.open('photo5.png')
    bw_img = img.convert('L')
    bw_img.save('bwphoto5.png')
    my_label.after(1000, show_pic1)

def show_pic1():
    global img2
    img2 = PhotoImage(file='bwphoto5.png')
    my_label.config(image=img2)
 
def wm(): 
    im = Image.open('photo5.png')
    fontt = ImageFont.truetype('arial.ttf', 46)
    textt = "Watermark"
    edit = ImageDraw.Draw(im)
    edit.text((150, 300), textt, ("white"), font=fontt)
    im.save('wmphoto5.png')
    my_label.after(1000, show_pic2)

def show_pic2():
    global im2
    im2 = PhotoImage(file='wmphoto5.png')
    my_label.config(image=im2)

def sz():
    my_im = Image.open('photo5.png')
    new_size = my_im.resize((400, 400))
    new_size.save('szphoto5.png')

    my_label.after(1000, show_pic3)

def show_pic3():
    global my_im2
    my_im2 = PhotoImage(file='szphoto5.png')
    my_label.config(image=my_im2)

myButton = Button(root, text='Watermark', padx=50, pady=20, command=wm)
myButton.pack(side=TOP)
myButton2 = Button(root, text='B/W', padx=50, pady=20, command=bw)
myButton2.pack(side=LEFT)
myButton3 = Button(root, text='Size', padx=50, pady=20, command=sz)
myButton3.pack(side=BOTTOM)
root .mainloop()
