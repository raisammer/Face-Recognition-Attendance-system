#importing required library
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
from datetime import datetime
from win32com.client import Dispatch

#-->used streamlit library for frontend
# giving the title
# print(os.getcwd())
st.title("FACE ATTENDANCE SYSTEM")

#inserting an invisble container so to insert image
st.image("data:image/jpeg;base64,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")

#creating a checkbox
run = st.button('Start')

#if the checkbox--> pressed
#run the inner command
if run :
    # print("here2")
    #the path where the database is stored
    #use full address if it is not in your directory
    path = 'image_attendance'

    # craeting an empty list of images and image names
    images = []
    image_name = []

    #folder pointing towards the file where the database is stored
    folder = os.listdir(path)
    # print(folder)

    #Going to the folder and appending the images and the name corresponding to the image #Think of appending roll number too

    for NAME in folder:
        running_img = cv2.imread(f'{path}/{NAME}')
        # print(running_img)
        images.append(running_img)
        # taking the first part of the name so that only name could come
        image_name.append(os.path.splitext(NAME)[0])
    # print(image_name)
    # print(images)


    #As we are going with face_recognition library
    #face_recognition recognises the faces and find important points (corner points)66 such points are there f or finding the features
    #making a function which will take the encoding from the image
    def take_encoding(images):
        encoding_list =[]
        for i in images:
            img = cv2.cvtColor(i ,cv2.COLOR_BGR2RGB)
            image_encoding = face_recognition.face_encodings(img)[0]
            encoding_list.append(image_encoding)
        return encoding_list


    # taking the encoding of the databases
    known_encoding = take_encoding(images)
    print('Encoding has been done ')


    #  defining the attendance system for recording the attendance
    def Attendance_system(name):
        # opening attendance file with read as well as write functionality
        with open('attendance_sheet.csv', 'r+') as f:
            # making first_col list -->to store the entry
            first_col = []
            # read the entered data
            entered_data = f.readlines()

        # making columns by seprating with comma in excel sheet
            for row in entered_data:
                entry = row.split(',')
                first_col.append(entry[0])

            # if name is not in list then it will record otherise it will continusously record the attendamnce of the same person
            if name not in first_col:
                timing = datetime.now()
                date_time_String = timing.strftime('%H:%M:%S')
                date = timing.strftime('%d-%B-%Y')
                # speak("Attendance marked")
                # writing the date time in the attendance sheet
                f.writelines(f'\n{name},{date_time_String},{date}')
            # f.close()

    print("here")
    # starting the video
    cap = cv2.VideoCapture(0)
    window = st.image([])
    while True:
        ret, img = cap.read()
        # flipped the image
        img = cv2.flip(img,1)
        # taken the size as(0,0) so that the program can run fast and xsize ysize reduce to 0.25
        current_image = cv2.resize(img, (0, 0), None, 0.2, 0.2)
        current_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)

        # finding face encoding and location of the current image
        faces_loc_current_image = face_recognition.face_locations(current_image)
        face_encoding_current_image = face_recognition.face_encodings(current_image, faces_loc_current_image)

        #Comparing the trained faces and the current face encoding  and distance between the faces
        for current_face_encoding, face_loc in zip(face_encoding_current_image, faces_loc_current_image):
            comparing = face_recognition.compare_faces(known_encoding, current_face_encoding)
            distance_face = face_recognition.face_distance(known_encoding, current_face_encoding)
            print(distance_face)
            #the minimum distance for the current image will correspond to the image of the person in the current image
            matchIndex = np.argmin(distance_face)

            # the distance will be less than 0.5 than the  image will show the  name with the minimum distance otherwise it will show unknown
            if distance_face[matchIndex] < 0.6:
                name = image_name[matchIndex].upper()

            else:
                name ="Unknown"
            print(name)
            # taking the coordinate of the face
            y1, x2, y2, x1 = face_loc

            #multiplying these by 5 as the rectangle will become smaller as we have reduced the y and x by 5 times for increasing the speed
            y1 = y1 * 5
            x2 = x2 * 5
            y2 = y2 * 5
            x1 = x1 * 5
            #drawing the rectangle around the face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # drawing the rectangle around the names and filling it will the green color
            cv2.rectangle(img, (x1, y2 - 30), (x2, y2), (0, 255, 0), cv2.FILLED)
            #giving the text for the name
            cv2.putText(img, name, (x1 + 5, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
            #calling the attendance sheet to register the attendance
            Attendance_system(name)
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        # this will show the image at the web page
        window.image(img)
    cap.release()