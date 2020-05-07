# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
import matplotlib.pyplot as plt



def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        image2 = cv2.imread(path)

        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()


        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        kp2, des2 = sift.detectAndCompute(gray2, None)
        image2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        image2 = Image.fromarray(image2)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        image2 = ImageTk.PhotoImage(image2)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=image2)
            panelB.image = image2
            panelB.pack(side="right", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=image2)
            panelA.image = image
            panelB.image = image2

def select_image2():
    # grab a reference to the image panels
    global panelC, panelD

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        image2 = cv2.imread(path)

        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()


        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        kp2, des2 = sift.detectAndCompute(gray2, None)
        image2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        image2 = Image.fromarray(image2)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        image2 = ImageTk.PhotoImage(image2)

        # if the panels are None, initialize them
        if panelC is None or panelD is None:
            # the first panel will store our original image
            panelC = Label(image=image)
            panelC.image = image
            panelC.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelD = Label(image=image2)
            panelD.image = image2
            panelD.pack(side="right", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelC.configure(image=image)
            panelD.configure(image=image2)
            panelC.image = image
            panelD.image = image2

def grafik():
    # grab a reference to the image panels

    # open a file chooser dialog and allow the user to select an input
    # image
    img = panelA
    img2 = panelC

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()

    kp, des = sift.detectAndCompute(gray, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    matches = bf.match(des, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    img3 = cv2.drawMatches(gray, kp, img2, kp2, matches[:50], img2, flags=2)
    plt.imshow(img3), plt.show()

def new():
    top = Toplevel()
    top.title('new window')

# initialize the window toolkit along with the two image panels
root = Tk()
root.title('Face Detection By Image')
root.iconbitmap('images/interface.ico')
panelA = None
panelB = None
panelC = None
panelD = None
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open File Gambar 1", command=select_image)
subMenu.add_command(label="Open File Gambar 2", command=select_image2)
subMenu.add_command(label="Look Grafik", command=grafik)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)
# kick off the GUI
root.mainloop()