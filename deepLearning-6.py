import cv2
import jetson_inference as jet_inf
import jetson_utils as jet_uti
import time
import numpy as np


width = int(640 * 2)
height = int(480 * 1.5)
dispW = width
dispH = height
flip = 0
timeStamp = time.time()
fpsFltr = 0
font = cv2.FONT_HERSHEY_SIMPLEX

net = jet_inf.detectNet('trafficcamnet', threshold=0.5)
#'ssd-mobilenet-v1','ssd-inception-v2','peoplenet','peoplenet-pruned','dashcamnet','trafficcamnet','facedetect'

""" camSet = ('nvarguscamerasrc wbmode=9 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !'
          ' video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 !'
          ' nvvidconv flip-method='+ str(flip) +' !'
          ' video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx !'
          ' videoconvert ! video/x-raw, format=BGR !'
          ' videobalance contrast=1.5 brightness=-0.2 saturation=1.2 ! appsink drop=1')
cam0 = cv2.VideoCapture(camSet) """
# FOR GST CAMERA
#cam0 = jet_uti.gstCamera(dispW, dispH, '0')
#cam1 = jet_uti.gstCamera(dispW, dispH, '/dev/video1')
#cam2 = jet_uti.gstCamera(dispW, dispH, '/dev/video2')
#display = jet_uti.glDisplay()

cam1 = cv2.VideoCapture('/dev/video1')
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, dispW) # or cam1.set(3, dispW)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH) # or cam1.set(4, dispH)
#cam2 = cv2.VideoCapture('/dev/video2')
#cam2.set(cv2.CAP_PROP_FRAME_WIDTH, dispW) # or cam2.set(3, dispW)
#cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH) # or cam2.set(4, dispH)

# FOR GST CAMERA
#while display.IsOpen():
while True:
    #_, img = cam0.read()
    _, img = cam1.read()
    #_, img = cam2.read()
    # FOR GST CAMERA
    #img, width, height = cam0.CaptureRGBA()
    #img, width, height = cam1.CaptureRGBA()
    #img, width, height = cam2.CaptureRGBA()
    height = img.shape[0]
    width = img.shape[1]
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame = jet_uti.cudaFromNumpy(frame)
    detections = net.Detect(frame, width, height)

    for detect in detections:
        ID = detect.ClassID
        top = int(detect.Top)
        left = int(detect.Left)
        bottom = int(detect.Bottom)
        right = int(detect.Right)
        item = net.GetClassDesc(ID)
        print(item, top, left, bottom, right)

    # FOR GST CAMERA
    #display.RenderOnce(img, width, height)
    dt = time.time() - timeStamp
    timeStamp = time.time()
    fps = 1 / dt
    fpsFltr = 0.9*fpsFltr + 0.1*fps
    #print(str(round(fps, 1)) + ' fps ')
    cv2.putText(img, str(round(fpsFltr, 1)) + ' fps ', (0, 30), font, 1, (0, 0, 255), 2)
    #cv2.imshow('cam0', img)
    cv2.imshow('cam1', img)
    #cv2.imshow('cam2', img)
    #cv2.moveWindow('cam0', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

    if KeyboardInterrupt is True:
        break

#cam0.release()
cam1.release()
#cam2.release()
cv2.destroyAllWindows()
