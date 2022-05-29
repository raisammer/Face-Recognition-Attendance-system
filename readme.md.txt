#face Recognition Attendance system

Face recognition attendance system is a effective way of doing the attendance which saves times .
The thing which we need to do for the attendance to come in front of the camera and that will be going to do all our work

##why i have choosen face_recogniton library 

I have proceeded with face recognition library because the model has an accuracy of 99.38% on the Labeled faces in the wild Benchmark
This model just take the single photo and find the important points(end points )which are generally 66points and then find the matching with one or known faces in a database

 
## Steps to build the face _recogniton attendance system model
###Install Libraries

**opencv--python
**face_recognition
**cmake
**dlib
**numpy
**streamlit for frontend development

##Steps involoved  :
### step 1: Importing the libraray 
### step 2: Give the design for the web page to be hosted 
### step 3: Importing the images from the local data base
### step 4: Computed the encoding of the database image and storing the encoding 
### step 5: Hosting the web cam and find the encoding of the current frame
### step 6: Finding the matches between the known encoding and current frame encoding
### step 7: The one who suitably matches with the database the attendance have been marked for that one 
### step 8:  The attendance will be marked up in the attendance sheet(i.e, excel sheet for our case) .

##why i haven't choose to go with face api
When we use any face api then there are api hit limits, so to get rid of that i have made my owned backend model
for face recognition using face recognition library which is giving me upto 99.38% accuracy  
 

##why i proceded with streamlit framework for front end deployment
I have proceeded with streamlit as i have learnt the python and c++ and having less knowledge of web development 
so streamlit provides the way to make the frontend using the python and it is an open source python library for creating web apps .
 