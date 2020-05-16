# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
import matplotlib.pyplot as plt
import face_recognition



def select_image_new():
    # grab a reference to the image panels
    global panelA, panelB

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk
        # edges in it

        imageinput = face_recognition.load_image_file(path)
        imageoutput = face_recognition.load_image_file(path)


        # declare to sift
        grayoutput = cv2.cvtColor(imageoutput, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()

        # declare imageoutput in read face location
        face_locations = face_recognition.face_locations(imageoutput, number_of_times_to_upsample=0, model="cnn")
        # face_locations2 = face_recognition.face_locations(image)


        #  represents images in face location
        print(face_locations)
        for i in range(len(face_locations)):
            imageinput = cv2.rectangle(imageinput, (face_locations[i][1], face_locations[i][0]),
                                  (face_locations[i][3], face_locations[i][2]), (255, 0, 255), 2)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            top, right, bottom, left = face_location

            print(
                "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,right))
        face_image = imageoutput[top:bottom, left:right]

        # change itu image from array
        imageinput = Image.fromarray(imageinput)
        kp2, des2 = sift.detectAndCompute(grayoutput, None)
        imageoutput = cv2.drawKeypoints(face_image, kp2, flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS, outImage=None)
        imageoutput = Image.fromarray(imageoutput)

        # ...and then to ImageTk format
        imageinput = ImageTk.PhotoImage(imageinput)
        imageoutput = ImageTk.PhotoImage(imageoutput)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image

            panelA = Label(image=imageinput)
            panelA.image = imageinput
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=imageoutput)
            panelB.image = imageoutput
            panelB.pack(side="left", padx=10, pady=10)

        else:
            # update the pannels
            panelA.configure(image=imageinput)
            panelB.configure(image=imageoutput)

            panelA.image = imageinput
            panelB.image = imageoutput

        cv2.imwrite('in.jpg', imageinput)
        cv2.imwrite('out.jpg', imageoutput)

# initialize the window toolkit along with the two image panels
root = Tk()
root.title('Face Detection By Image')
root.iconbitmap('images/interface.ico')
panelA = None
panelB = None
menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Choose File", command=select_image_new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)
# kick off the GUI
root.mainloop()