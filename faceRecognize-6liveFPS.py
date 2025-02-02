import os
import time
import pickle
import face_recognition as face_rec
import cv2
print(cv2.__version__)

FRAME_WIDTH = 640
FRAME_HEIGHT = 480
Encodings = []
Names = []
fpsReport = 0
scaleFactor = 0.666

with open('/home/your_user_name/Desktop/pyProg/faceRecognizer/demoImages/train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

timeStamp = time.time()

while True:
    _, frame = cam.read()
    frameSmall = cv2.resize(frame, (0, 0), fx = scaleFactor, fy = scaleFactor)
    frameRGB = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB)
    #frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    facePositions = face_rec.face_locations(frameRGB, model='CNN')
    allEncodings = face_rec.face_encodings(frameRGB, facePositions)

    for (top, right, bottom, left), face_encoding in zip(facePositions, allEncodings):
        name = 'Unknown Person'
        matches = face_rec.compare_faces(Encodings, face_encoding)

        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]
        top = int(top / scaleFactor)
        bottom = int(bottom / scaleFactor)
        right = int(right / scaleFactor)
        left = int(left / scaleFactor)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top-6), font, 1, (0, 255, 255), 2)

    dt = time.time() - timeStamp
    fps = 1 / dt
    fps = round(fps, 2)
    fpsReport = (0.90 * fpsReport) + (0.10 * fps)
    #print('fps is: ', round(fpsReport, 1))
    timeStamp = time.time()

    cv2.rectangle(frame, (0, 0), (100, 40), (255, 0, 0), -1)
    cv2.putText(frame, str(round(fpsReport, 1)) + 'fps', (0, 25), font, 1, (0, 255, 255), 2)
    cv2.imshow('Picture', frame)
    #cv2.moveWindow('Picture', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

    if KeyboardInterrupt is True:
        break

cam.release()
cv2.destroyAllWindows()

