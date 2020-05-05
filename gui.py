from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title('Face Detection By Image')
root.iconbitmap('images/interface.ico')
root.geometry("450x450")

image = []
def addFileImage():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(title="Select File")
    image.append(filename)
    print(filename)
    for app in image:
        label = tk.Label(frame, text=app)
        label.pack()
    # img = ImageTk.PhotoImage(Image.open(filename))
    # label = Frame(image=img)
    # label.pack(label)
# def openImg():
#     x = addFileImage()
#     img = Image.open(x)
#     img = ImageTk.PhotoImage(img)
#     print(img)
#     panel = Label(Frame, image=img)
#     panel.image = img

# Main Menu
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open File", command=addFileImage)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

# Toolbar
# toolbar = Frame(root, bg="blue")
#
# def doNothing(args):
#     pass
#
# insertButt = Button(toolbar, text="Insert Image", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)
# toolbar.pack(side=TOP, fill=X)

# load image
# img1 = ImageTk.PhotoImage(Image.open("./resources/image/1.jpg"))
# img2 = ImageTk.PhotoImage(Image.open("./resources/image/01.jpg"))
# img3 = ImageTk.PhotoImage(Image.open("./resources/image/2.jpg"))
# image_list = [img1, img2, img3]
#
# img_label = Label(image=img1)
# img_label.grid(row=0, column=0, columspan=3)

canvas = tk.Canvas(root, height=800, width=800, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)
root.mainloop()