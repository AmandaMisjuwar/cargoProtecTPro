''''
cargoProtecTPro - Delta Hacks 5 2019
***************************************

Created BY: MOhammed Perves, Amanda Masjuwar, Jessica Li, Amanda Guo
'''

import cv2
import numpy as np
from PIL import Image
import os


def train_model():
    # Path for face image database
    path = "dataset/"

    # recognizer = cv2.createLBPHFaceRecognizer()
    # create our LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # or use EigenFaceRecognizer by replacing above line with
    # face_recognizer = cv2.face.createEigenFaceRecognizer()

    # or use FisherFaceRecognizer by replacing above line with
    # face_recognizer = cv2.face.createFisherFaceRecognizer()

    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    # function to get the images and label data
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:
            print(imagePath)
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids

    print("\n Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml')  # recognizer.save() worked on Mac, but not on Pi

    # Print the numer of faces trained and end program
    print("\n Model trained with {0} faces. Exiting Program".format(len(np.unique(ids))))

    return
