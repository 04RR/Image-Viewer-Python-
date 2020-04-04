import tkinter as tk
from PIL import Image, ImageTk
from resizeimage import resizeimage

win = tk.Tk()
win.title('Image Viewer')
win.geometry('500x500')

path = '#Your image path'
resize_image = resizeimage.resize_cover(Image.open(path), [500,500])
render_pic = ImageTk.PhotoImage(resize_image)
img = tk.Label(win, image=render_pic)
img.pack()

win.mainloop()
