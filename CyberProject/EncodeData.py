'''
author: @AP
4-10-2019
'''
import os
import face_recognition
import cv2
import time
import numpy as np
import pickle
import uuid
import Classes
from pip._internal.utils.misc import read_text_file

ListOfPeople = []
'''
class person:
   
    def __init__(self, name, encodings, uuid, info, picture):
        self.Name = name
        self.FaceEncodings = encodings
        self.UUID = uuid
        self.Info = info
        self.Picture = picture
        '''
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def ProcessData(DataPath):
    global LisOfPeople
    '''
        encode all faces
    '''
    options = []
    path = (DataPath)
    usb = os.listdir(path)
    #insert path to usb
    #print(usb)
    if 'FaceData.txt' in usb:
         text_file = read_text_file(os.path.join(path,'FaceData.txt'))
         options = text_file.splitlines()
    if 'NoChange' in options:
        '''
            conditions to not encode faces and just read in an existing data set
        '''
    for folder in usb:
        #get folder name and assign that to the person
        #print(folder)
        if not folder.endswith(('.txt', '.dat', '.jpg', '.jpeg')) and folder != 'System Volume Information':
            CurEncodings = []
            PersonIdentity = folder
            DataPath = os.path.join(path, folder)
            Information = os.listdir(DataPath)
            UniqueID = uuid.uuid4()
            Info = ''
            img = []
            for data in Information:
                '''
                    start assigning datas
                '''
                #print(data)
                if data.endswith(('.jpg', '.jpeg', '.png')):
                    to_encode = face_recognition.load_image_file(os.path.join(DataPath, data))
                    CurEncodings.append(face_recognition.face_encodings(to_encode)[0])
                    img = cv2.imread(data)
                if (data == 'Data.txt'):
                    '''
                    '''
                    Info = read_text_file(os.path.join(DataPath,'Data.txt'))
                    
                                                            
            #tbc
            ListOfPeople.append(Classes.person(PersonIdentity, CurEncodings, UniqueID, Info, img))


def SaveData():
    global ListOfPeople
    with open('Dox.dat', 'wb') as f:
        pickle.dump(ListOfPeople, f)

def Main():
    DataPath = ''
    user_input = -1
    while user_input not in range(0,3):
          print('User Menu' + '\n' + '--------' + '\n' + '(1) Process Data' + '\n'+'(2) Set Data Path' + '\n' + '(3) Exit')
          user_input = input('')
          user_input = int(user_input)
          #print(user_input)
          if user_input == 1:
              if DataPath == '':
                  user_input = ''
                  while user_input.lower() != 'y' or 'n':
                       print('Data Path Not Set' + '\n' + 'continue?(Y/N)')
                       user_input = input('')
                       if user_input.lower() == 'n':
                           Path_input = input('Enter Data Path: ')
                           DataPath = Path_input
                           break
                       if user_input.lower() == 'y':
                           break
              print('Encoding Data')
              ProcessData(DataPath)
              print('Saving Data')
              SaveData()
              print('Complete!')
              break
          if user_input == 2:
              Path_input = input('Enter Data Path: ')
              DataPath = Path_input
              print('Encoding Data')
              ProcessData(DataPath)
              print('Saving Data')
              SaveData()
              print('Complete!')
              break
          if user_input == 3:
              exit()
                
            
Main()
