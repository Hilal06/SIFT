# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
import matplotlib.pyplot as plt
import face_recognition

def select_image():
    # grab a reference to the image panels
    global panelA, panelB, panelC

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        # image = cv2.imread(path)
        # image2 = cv2.imread(path)
        image = face_recognition.load_image_file(path)
        image2 = face_recognition.load_image_file(path)
        image3 = cv2.imread(path)

        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()

        face_locations = face_recognition.face_locations(image2, number_of_times_to_upsample=0, model="cnn")
        # face_locations2 = face_recognition.face_locations(image)


        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(face_locations)
        for i in range(len(face_locations)):
            image = cv2.rectangle(image, (face_locations[i][1], face_locations[i][0]),
                                  (face_locations[i][3], face_locations[i][2]), (255, 0, 255), 2)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            top, right, bottom, left = face_location

            print(
                "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                      right))

        face_image = image2[top:bottom, left:right]

        # convert the images to PIL format...
        image = Image.fromarray(image)
        image2 = Image.fromarray(face_image)
        kp2, des2 = sift.detectAndCompute(gray3, None)
        image3 = cv2.drawKeypoints(face_image, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        image3 = Image.fromarray(image3)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        image2 = ImageTk.PhotoImage(image2)
        image3 = ImageTk.PhotoImage(image3)

        # if the panels are None, initialize them
        if panelA is None or panelB or panelC is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=image2)
            panelB.image = image2
            panelB.pack(side="left", padx=10, pady=10)

            panelC = Label(image=image3)
            panelC.image = image3
            panelC.pack(side="right", padx=10, pady=10)
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=image2)
            panelC.configure(image=image3)
            panelA.image = image
            panelB.image = image2
            panelC.image = image3

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
        # kp2, des2 = sift.detectAndCompute(gray2, None)
        # image2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        kp = sift.detect(gray2,None)

        image2=cv2.drawKeypoints(gray2,kp,image2,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
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
    global panelA, panelB, panelC

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        # image = cv2.imread(path)
        # image2 = cv2.imread(path)
        image = face_recognition.load_image_file(path)
        image2 = face_recognition.load_image_file(path)
        image3 = cv2.imread(path)

        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()

        face_locations = face_recognition.face_locations(image2, number_of_times_to_upsample=0, model="cnn")
        # face_locations2 = face_recognition.face_locations(image)

        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(face_locations)
        for i in range(len(face_locations)):
            image = cv2.rectangle(image, (face_locations[i][1], face_locations[i][0]),
                                  (face_locations[i][3], face_locations[i][2]), (255, 0, 255), 2)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            top, right, bottom, left = face_location

            print(
                "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                      right))

        face_image = image2[top:bottom, left:right]

        # convert the images to PIL format...
        image = Image.fromarray(image)
        image2 = Image.fromarray(face_image)

        kp, des = sift.detectAndCompute(gray1, None)
        kp2, des2 = sift.detectAndCompute(gray3, None)

        img = cv2.drawKeypoints(gray1, kp, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        image3 = cv2.drawKeypoints(face_image, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        # image3 = Image.fromarray(image3)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        image2 = ImageTk.PhotoImage(image2)
        # image3 = ImageTk.PhotoImage(image3)
        cv2.imwrite('sift1.jpg', img)
        cv2.imwrite('sift2.jpg', image3)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(des, des2, k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]

        # ratio test as per Lowe's paper
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.8 * n.distance:
                matchesMask[i] = [1, 0]

        draw_params = dict(
            singlePointColor=(255, 0, 0),
            matchesMask=matchesMask,
            flags=0)

        img_res = cv2.drawMatchesKnn(gray1, kp, gray3, kp2, matches, None, **draw_params)

        # if the panels are None, initialize them
        if panelA is None or panelB or panelC is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=image2)
            panelB.image = image2
            panelB.pack(side="left", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=image2)
            panelA.image = image
            panelB.image = image2



        plt.imshow(img_res)
        plt.show()
        cv2.destroyAllWindows()

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
# subMenu.add_command(label="Open File Gambar 1", command=face)
subMenu.add_command(label="Open File Gambar 2", command=select_image2)
subMenu.add_command(label="Look Grafik", command=grafik)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)
# kick off the GUI
root.mainloop()



