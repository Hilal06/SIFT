import face_recognition
import cv2
import os
from PIL import Image, ImageDraw

# 1. Facial feature detection / Facial landmark detection / Facial keypoint detection.
# image = face_recognition.load_image_file("images/prilly4.jpg")
# image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#
# face_landmarks_list = face_recognition.face_landmarks(image)
# print(face_landmarks_list,"\n\n")
# #print(len(face_landmarks_list[0]['chin']))
#
# features_dict = dict()
#
# count = 0
# for i in range(0,len(face_landmarks_list)):
#     for feature in face_landmarks_list[0]:
#         count += 1
#         print("FEATURE is ", feature)
#         if feature in features_dict:
#             # append the new number to the existing array at this slot
#             #print("Appending...",face_landmarks_list[0][feature])
#             for j in range(0, len(face_landmarks_list[i][feature])):
#                 features_dict[feature].append(face_landmarks_list[i][feature][j])
#         else:
#             # create a new array in this slot
#             features_dict[feature] = face_landmarks_list[i][feature]
#
# print("Ran", count, "times")
#
# count = 0
# for feature in features_dict:
#     print(feature)
#     count += 1
#     for x in features_dict[feature]:
#         #print('X is ',x)
#         #print("Len of X is ",len(x))
#         #if(len(x)==2):
#         cv2.circle(image, x, 1, (0, 255, 0), 2)
#
# print(count)
# cv2.imshow('Output', image)
# cv2.waitKey(0)

# 2. Identify single & Multiple faces in an image.
# image = face_recognition.load_image_file("images/prilly4.jpg")
# face_locations = face_recognition.face_locations(image)
# image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#
# print(face_locations)
#
# for i in range(len(face_locations)):
#     image=cv2.rectangle(image,(face_locations[i][1],face_locations[i][0]),(face_locations[i][3],face_locations[i][2]),(255,0,255),2)
#
# cv2.imshow('Output',image)
# cv2.waitKey(0)

# 3. Find / Search an image within image gallery
# make a list of all the available images
# images = os.listdir('.\celebrities')
# print(images)
#
# image_to_be_matched=face_recognition.load_image_file('.\Test2.jpeg')
# #Convert target image to feature vector
# image_to_be_matched_encoded=face_recognition.face_encodings(image_to_be_matched)[0]
#
# # iterate over each image
# for image in images:
#     # load the image
#     current_image = face_recognition.load_image_file('.\celebrities\\' + image)
#
#     # encode the loaded image into a feature vector
#     current_image_encoded = face_recognition.face_encodings(current_image)[0]
#
#     # match your image with the image and check if it matches
#     result = face_recognition.compare_faces(
#         [image_to_be_matched_encoded], current_image_encoded)
#
#     # check if it was a match
#     if result[0] == True:
#         print("Matched: " + image)
#     else:
#         print("Not matched: " + image)


# 4. Find all the faces in an image
# Load the jpg file into a numpy array
# image = face_recognition.load_image_file("images/prilly4.jpg")
#
# # Find all the faces in the image using the default HOG-based model.
# face_locations = face_recognition.face_locations(image)
# print(face_locations)
# print("I found {} face(s) in this photograph.".format(len(face_locations)))
#
# for face_location in face_locations:
#
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#
#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.show()


# 5. Digital MakeUp

# # Load the jpg file into a numpy array
# image = face_recognition.load_image_file("images/prilly4.jpg")
#
# # Find all facial features in all the faces in the image
# face_landmarks_list = face_recognition.face_landmarks(image)
#
# for face_landmarks in face_landmarks_list:
#     pil_image = Image.fromarray(image)
#     d = ImageDraw.Draw(pil_image, 'RGBA')
#
#     # Make the eyebrows into a nightmare
#     d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
#     d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
#     d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
#     d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)
#
#     # Gloss the lips
#     d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
#     d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
#     d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
#     d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)
#
#     # Sparkle the eyes
#     d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
#     d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))
#
#     # Apply some eyeliner
#     d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
#     d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)
#
#     pil_image.show()

# 6. Using CNN
# # Load the jpg file into a numpy array
# image = face_recognition.load_image_file("images/prilly4.jpg")
# #
# # # Find all the faces in the image using a pre-trained convolutional neural network.
# # # This method is more accurate than the default HOG model, but it's slower
# # # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
# # # this will use GPU acceleration and perform well.
# # # See also: find_faces_in_picture.py
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
# #
# print("I found {} face(s) in this photograph.".format(len(face_locations)))
# #
# for face_location in face_locations:
# #
# #     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# #
# #     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.show()
