import time
import sys
from threading import Thread
import cv2
import numpy as np


class vStream:
    ''' Capture streaming video class'''

    def __init__(self, src, width, height):
        ''' Init method '''
        self.width = width
        self.height = height
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        ''' Read capture streaming '''
        while True:
            _, self.frame = self.capture.read()
            self.frame2 = cv2.resize(self.frame, (self.width, self.height))

    def getFrame(self):
        ''' Get frame from the source '''
        return self.frame2


flip = 0
dispH = 480
dispW = 640
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam1 = vStream(1, dispW, dispH)
cam2 = vStream(camSet, dispW, dispH)
font = cv2.FONT_HERSHEY_SIMPLEX
startTime = time.time()
dtav = 0

while True:
    try:
        myFrame1 = cam1.getFrame()
        myFrame2 = cam2.getFrame()
        myFrame3 = np.hstack((myFrame1, myFrame2))
        dt = time.time() - startTime
        startTime = time.time()
        dtav = 0.9*dtav + 0.1*dt
        fps = 1 / dtav
        #print(round(fps, 2))
        cv2.rectangle(myFrame3, (0, 0), (140, 40), (255, 0, 0), -1)
        cv2.putText(myFrame3, str(round(fps, 1)) + 'fps', (0, 25), font, 1, (0, 255, 255), 2)
        #cv2.imshow('webCam', myFrame1)
        #cv2.imshow('piCam', myFrame2)
        cv2.imshow('comboCam', myFrame3)
    except:
        print('frame not available')

    if cv2.waitKey(1) == ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        sys.exit("Good to go")
        break

    if KeyboardInterrupt is True:
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        sys.exit('Good to go')
        break
