''''
cargoProtecTPro - Delta Hacks 5 2019
***************************************

Created BY: MOhammed Perves, Amanda Masjuwar, Jessica Li, Amanda Guo
'''
import cv2
import os


def gen_data():
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = input("Enter user ID: ")

    print("\n Initializing face capture. Look at the camera and press <SPACE> to take picture of face...")
    # Initialize individual sampling face count
    count = 0

    while count < 30:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # flip video image horizontally
        # cv2.imshow("Camera", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        cv2.imshow("Camera", frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the captured image into the datasets folder
            k = cv2.waitKey(0)
            if k == 32:  # 32 for space /27 Esc key to stop
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imshow('Image', gray)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    # Do a bit of cleanup
    print("\nExiting Program and cleanup stuff")
    cap.release()
    cv2.destroyAllWindows()

    return
