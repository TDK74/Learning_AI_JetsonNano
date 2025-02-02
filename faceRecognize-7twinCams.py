import numpy as np
import time
import cv2
print(cv2.__version__)


dispW = 640
dispH = 480
flip = 0
font = cv2.FONT_HERSHEY_SIMPLEX
dtav = 0

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
piCam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)
usbCam = cv2.VideoCapture(1)
#usbCam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#usbCam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

startTime = time.time()

while True:
    ret, framePi = piCam.read()
    ret, frameUsb = usbCam.read()
    #print(framePi.shape)
    frameUsb = cv2.resize(frameUsb, (framePi.shape[1], framePi.shape[0]))
    frameCombined = np.hstack((framePi, frameUsb))

    dt = time.time() - startTime
    startTime = time.time()
    dtav = 0.9 * dtav + 0.1 * dt
    fps = 1 / dtav

    cv2.rectangle(frameCombined, (0, 0), (130, 40), (255, 0, 0), -1)
    cv2.putText(frameCombined, str(round(fps, 1)) + 'FPS', (0, 25), font, 1, (0, 255, 255), 2)
    cv2.imshow('Combo', frameCombined)
    cv2.moveWindow('Combo', 0, 0)
    #cv2.imshow('PiCam', framePi)
    #cv2.imshow('UsbCam', frameUsb)
    #cv2.moveWindow('PiCam', 0, 0)
    #cv2.moveWindow('UsbCam', 0, 500)

    if cv2.waitKey(1) == ord('q'):
        break

    if KeyboardInterrupt is True:
        break

piCam.release()
usbCam.release()
cv2.destroyAllWindows()
