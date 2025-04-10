import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'known faces'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    img = cv2.imread(f'{path}/{climages.append(img)
            classNames.append(os.path.splitext(cl)[0])

            def findEncodings(images):
                encodeList = []
                    for img in images:
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                                    encodeList.append(face_recognition.face_encodings(img)[0])
                                        return encodeList

                                        encodeListKnown = findEncodings(images)
                                        print("Encoding Complete")

                                        def markAttendance(name):
                                            with open('Attendance.csv', 'a+') as f:
                                                    f.seek(0)
                                                            data = f.readlines()
                                                                    names = [line.split(',')[0] for line in data]
                                                                            if name not in names:
                                                                                        now = datetime.now()
                                                                                                    timeStr = now.strftime('%H:%M:%S')
                                                                                                                dateStr = now.strftime('%Y-%m-%d')
                                                                                                                            f.writelines(f'\n{name},{timeStr},{dateStr}')

                                                                                                                            cap = cv2.VideoCapture(0)

                                                                                                                            while True:
                                                                                                                                success, img = cap.read()
                                                                                                                                    imgSmall = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
                                                                                                                                        imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

                                                                                                                                            facesCurFrame = face_recognition.face_locations(imgSmall)
                                                                                                                                                encodesCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)

                                                                                                                                                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                                                                                                                                                            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                                                                                                                                                                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                                                                                                                                                                            matchIndex = np.argmin(faceDis)
                                                                                                                                                                                    if matches[matchIndex]:
                                                                                                                                                                                                name = classNames[matchIndex].upper()
                                                                                                                                                                                                            y1, x2, y2, x1 = [v * 4 for v in faceLoc]
                                                                                                                                                                                                                        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                                                                                                                                                                                                                                    cv2.putText(img, name, (x1+6, y2+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                                                                                                                                                                                                                                                markAttendance(name)

                                                                                                                                                                                                                                                    cv2.imshow('Webcam', img)
                                                                                                                                                                                                                                                        if cv2.waitKey(1) == ord('q'):
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                