import cv2
import jetson_inference as jet_inf
import jetson_utils as jet_uti
import time
import numpy as np
import os
from gtts import gTTS
import threading


width = int(640 * 1)
height = int(480 * 1)
dispW = width
dispH = height
flip = 0
speak = True
confidence = 0
item = 'Welcome to my identify. Are you ready to rumble?'
itemOld = ''
fpsFltr = 0
timeMark = time.time()

def say_item():
    global speak
    global item

    while True:
        if speak is True:
            output = gTTS(text=item, lang='en', slow=False)
            output.save('output.mp3')
            os.system('mpg123 output.mp3')
            speak = False


thrd = threading.Thread(target=say_item, daemon=True)
thrd.start()

#Uncomment These next Two Line for Pi Camera
""" camSet = ('nvarguscamerasrc wbmode=9 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !'
          ' video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 !'
          ' nvvidconv flip-method='+ str(flip) +' !'
          ' video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx !'
          ' videoconvert ! video/x-raw, format=BGR !'
          ' videobalance contrast=1.5 brightness=-0.2 saturation=1.2 ! appsink drop=1')
cam = cv2.VideoCapture(camSet) """

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW) # or cam1.set(3, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH) # or cam1.set(4, dispW)

net = jet_inf.imageNet('googlenet')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cam.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jet_uti.cudaFromNumpy(img)

    if speak is False:
        classID, confidence = net.Classify(img, width, height)

        if confidence >= 0.5:
            item = net.GetClassDesc(classID)

            if item != itemOld:
                speak = True

        if confidence <= 0.5:
            item = ''

        itemOld = item

    dt = time.time() - timeMark
    fps = 1 / dt
    fpsFltr = 0.95*fpsFltr + 0.05*fps
    timeMark = time.time()
    cv2.putText(frame, str(round(fpsFltr, 1)) + ' fps ' + item + ' ' +
                str(round(confidence, 2)), (0, 30), font, 1, (0, 0, 255), 2)
    cv2.imshow('cam', frame)
    #cv2.moveWindow('cam', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
    if KeyboardInterrupt is True:
        break

cam.release()
cv2.destroyAllWindows()
