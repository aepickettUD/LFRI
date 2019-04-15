'''
author @ap
'''
import os
import face_recognition
import cv2
import numpy as np
class person:
    '''
        Name
        face encodings
        unique Identifier
        information
        picture
    '''
    def __init__(self, name, encodings, uuid, info, picture):
        self.Name = name
        self.FaceEncodings = encodings
        self.UUID = uuid
        self.Info = info
        self.Picture = picture
        
    def CompareFace(self, Face):
        return face_recognition.compare_faces(self.FaceEncodings, Face)
    def EmailContent(self):
        message = 'Name: ' + self.Name + '\n' + 'ID: ' + str(self.UUID) + '\n' + 'Bio: '+ self.Info
        return message
            

