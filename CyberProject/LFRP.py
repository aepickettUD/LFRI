import os
import face_recognition
import cv2
import time
import numpy as np
import pickle
import uuid
import Classes
import SendPerson
from pip._internal.utils.misc import read_text_file

ListOfPeople = []
ListOfPeopleFaces = []
video_capture = cv2.VideoCapture(0)
#the goal is to use index comparison to speed up the search process

def PreProcessing():
    global ListOfPeople
    with open('Dox.dat', "rb") as f:
        ListOfPeople = pickle.load(f)
    #print(ListOfPeople)
    #print(ListOfPeople[0].Picture)
    for people in ListOfPeople:
        ListOfPeopleFaces.append(people.FaceEncodings)

#PreProcessing()
def GetVideo():
    global video_capture
    global ListOfPeople
    global ListOfPeopleFaces
    PeopleSent = []
    face_locations = []
    face_encodings = []
    process_this_frame = 2 #process every 3rd frame
    while True:
        
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame == 0:
            InFrame = []
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                for people in ListOfPeople:
                    #print(people.Name)
                    #input('')
                    #print(people.CompareFace(face_encoding))
                    if people.CompareFace(face_encoding) == [True]:
                        InFrame.append(people)
                        
                        #print('person found')
            for people in InFrame:
                if people not in PeopleSent:
                    print('sending email')
                    #print(people.EmailContent())
                    cv2.imwrite('tempPic.jpg', frame)
                    SendPerson.Send(people)
                    PeopleSent.append(people)
                    os.remove('tempPic.jpg')
            process_this_frame = 3
            
        process_this_frame -= 1
        
def Main():
    
    PreProcessing()
    GetVideo()
Main()
