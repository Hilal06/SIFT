from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog
import cv2
import matplotlib.pyplot as plt
import face_recognition

def face():
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
        image_face = face_recognition.load_image_file(path)

        gray2 = cv2.cvtColor(image_face, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()

        face_landmarks_list = face_recognition.face_landmarks(image_face)
        print(face_landmarks_list, "\n\n")
        features_dict = dict()

        count = 0
        for i in range(0, len(face_landmarks_list)):
            for feature in face_landmarks_list[0]:
                count += 1
                print("FEATURE is ", feature)
                if feature in features_dict:
                    # append the new number to the existing array at this slot
                    # print("Appending...",face_landmarks_list[0][feature])
                    for j in range(0, len(face_landmarks_list[i][feature])):
                        features_dict[feature].append(face_landmarks_list[i][feature][j])
                else:
                    # create a new array in this slot
                    features_dict[feature] = face_landmarks_list[i][feature]
        print("Ran", count, "times")

        count = 0
        for feature in features_dict:
            print(feature)
            count += 1
            for x in features_dict[feature]:
                # print('X is ',x)
                # print("Len of X is ",len(x))
                # if(len(x)==2):
                cv2.circle(image_face, x, 1, (0, 255, 0), 2)

        print(count)

        #  represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        kp2, des2 = sift.detectAndCompute(gray2, None)
        # image_face = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
        image_face = Image.fromarray(image_face)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        image_face = ImageTk.PhotoImage(image_face)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=image_face)
            panelB.image = image_face
            panelB.pack(side="right", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=image_face)
            panelA.image = image
            panelB.image = image_face

# def select_image():
#     # grab a reference to the image panels
#     global panelA, panelB
#
#     # open a file chooser dialog and allow the user to select an input
#     # image
#     path = tkFileDialog.askopenfilename()
#
#     # ensure a file path was selected
#     if len(path) > 0:
#         # load the image from disk, convert it to grayscale, and detect
#         # edges in it
#         image = cv2.imread(path)
#         image2 = cv2.imread(path)
#
#         gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#         sift = cv2.xfeatures2d.SIFT_create()
#
#
#         #  represents images in BGR order; however PIL represents
#         # images in RGB order, so we need to swap the channels
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#         # convert the images to PIL format...
#         image = Image.fromarray(image)
#         kp2, des2 = sift.detectAndCompute(gray2, None)
#         image2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
#         image2 = Image.fromarray(image2)
#
#         # ...and then to ImageTk format
#         image = ImageTk.PhotoImage(image)
#         image2 = ImageTk.PhotoImage(image2)
#
#         # if the panels are None, initialize them
#         if panelA is None or panelB is None:
#             # the first panel will store our original image
#             panelA = Label(image=image)
#             panelA.image = image
#             panelA.pack(side="left", padx=10, pady=10)
#
#             # while the second panel will store the edge map
#             panelB = Label(image=image2)
#             panelB.image = image2
#             panelB.pack(side="right", padx=10, pady=10)
#
#         # otherwise, update the image panels
#         else:
#             # update the pannels
#             panelA.configure(image=image)
#             panelB.configure(image=image2)
#             panelA.image = image
#             panelB.image = image2

# def select_image():
#     # grab a reference to the image panels
#     global panelA, panelB
#
#     # open a file chooser dialog and allow the user to select an input
#     # image
#     path = tkFileDialog.askopenfilename()
#
#     # ensure a file path was selected
#     if len(path) > 0:
#         # load the image from disk, convert it to grayscale, and detect
#         # edges in it
#         image = cv2.imread(path)
#         # image2 = cv2.imread(path)
#         image2 = face_recognition.load_image_file(path)
#
#         gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#         sift = cv2.xfeatures2d.SIFT_create()
#
#         face_locations = face_recognition.face_locations(image2, number_of_times_to_upsample=0, model="cnn")
#
#         print("I found {} face(s) in this photograph.".format(len(face_locations)))
#
#         for face_location in face_locations:
#             top, right, bottom, left = face_location
#             print(
#                 "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
#                                                                                                       right))
#
#         face_image = image2[top:bottom, left:right]
#         #  represents images in BGR order; however PIL represents
#         # images in RGB order, so we need to swap the channels
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#         # convert the images to PIL format...
#         image = Image.fromarray(image)
#         kp2, des2 = sift.detectAndCompute(gray2, None)
#         image2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
#         image2 = Image.fromarray(face_image)
#
#         # ...and then to ImageTk format
#         image = ImageTk.PhotoImage(image)
#         image2 = ImageTk.PhotoImage(image2)
#
#         # if the panels are None, initialize them
#         if panelA is None or panelB is None:
#             # the first panel will store our original image
#             panelA = Label(image=image)
#             panelA.image = image
#             panelA.pack(side="left", padx=10, pady=10)
#
#             # while the second panel will store the edge map
#             panelB = Label(image=image2)
#             panelB.image = image2
#             panelB.pack(side="right", padx=10, pady=10)
#
#         # otherwise, update the image panels
#         else:
#             # update the pannels
#             panelA.configure(image=image)
#             panelB.configure(image=image2)
#             panelA.image = image
#             panelB.image = image2