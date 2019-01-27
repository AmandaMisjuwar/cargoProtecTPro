''''
cargoProtecTPro - Delta Hacks 5 2019
***************************************

Created BY: MOhammed Perves, Amanda Masjuwar, Jessica Li, Amanda Guo
'''
from imutils.object_detection import non_max_suppression
import imutils
import numpy as np
import cv2


def detect_humans():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    low_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # loop over the image paths
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture("http://172.17.98.28:8080/video")
    cap.set(3, 640)  # set video widht
    cap.set(4, 480)  # set video height

    # cap = cv2.VideoCapture("http://172.17.100.90:8080/shot.jpg")
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        # Capture frame-by-frame
        grabbed, frame = cap.read()
        # frame = cv2.resize(frame, (0, 0), fx=0.30, fy=0.3)
        frame = imutils.resize(frame, width=500)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = np.dstack([gray, gray, gray])
        # gray = cv2.flip(gray, 1)
        # frame = cv2.flip(frame, 1)

        # Display the resulting frame
        # cv2.imshow('Camera', frame)

        # cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # 1.1, 4
        # low = low_cascade.detectMultiScale(gray, 1.1, 3)

        # detect people in the frame
        (rects, weights) = hog.detectMultiScale(gray, winStride=(4, 4), padding=(5, 5), scale=1.05)

        # detect faces in the frame
        for (xF, yF, wF, hF) in faces:
            cv2.rectangle(gray, (xF, yF), (xF + wF, yF + hF), (12, 150, 100), 2)
            cv2.putText(gray, 'Face', (xF, yF), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # detect lower body in the frame
        # for (x, y, w, h) in low:
        # cv2.rectangle(gray, (x, y), (x + w, y + h), (12, 150, 100), 2)
        # cv2.putText(gray, 'Lower body', (x, y), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # draw the original bounding boxes
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Human', (x, y), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping
        # boxes that are still people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes after compression
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(gray, (xA, yA), (xB, yB), (0, 255, 0), 2)
            cv2.putText(gray, 'Human', (xA, yA), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # show some information on the number of bounding boxes
        # print("[INFO] : {} original boxes, {} after suppression".format(len(rects), len(pick)))

        # show the output images
        cv2.imshow("Colour - Human Detection", frame)
        cv2.imshow("Grayscale - Final (Compressed: Face & Lower Body)", gray)

        if cv2.waitKey(1) & 0xFF == ord('q') or not grabbed:
            break
    return
