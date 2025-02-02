import cv2
import jetson_inference as jet_inf
import jetson_utils as jet_uti
import time
import numpy as np


width = int(640 * 1)
height = int(480 * 1)
dispW = width
dispH = height
flip = 0

#Uncomment These next Two Line for Pi Camera
#camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam0 = cv2.VideoCapture(camSet)
#cam0 = jet_uti.gstCamera(width, height, '0')

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam1 = cv2.VideoCapture(1)
cam1.set(3, dispW)
cam1.set(4, dispH)
#cam1 = jet_uti.gstCamera(width, height, '/dev/video1')
#cam2 = jet_uti.gstCamera(width, height, '/dev/video2')
#display = jet_uti.glDisplay()
#font = jet_uti.cudaFont()
font = cv2.FONT_HERSHEY_SIMPLEX
net = jet_inf.imageNet('vgg-19')
#'alexnet','googlenet-12','resnet-18','resnet-50','resnet-101','resnet-152','vgg-16','vgg-19','inception-v4'
timeMark = time.time()
fpsFilter = 0

#while display.IsOpen():
while True:
    #frame, width, height= cam1.CaptureRGBA()
    #_, frame = cam0.read()
    _, frame = cam1.read()
    #frame, width, height= cam0.CaptureRGBA(zeroCopy=1)
    #frame, width, height= cam1.CaptureRGBA(zeroCopy=1)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jet_uti.cudaFromNumpy(img)
    #classID, confidence = net.Classify(frame, width, height)
    classID, confidence = net.Classify(img, width, height)
    item = net.GetClassDesc(classID)
    dt = time.time() - timeMark
    fps = 1 / dt
    fpsFilter = 0.95*fpsFilter + 0.5*fps
    timeMark = time.time()
    #font.OverlayText(frame, width, height, str(round(fpsFilter, 1)) + ' fps '
    #                 + item, 5, 5, font.Magenta, font.Blue)
    #display.RenderOnce(frame, width, height)
    #frame = jet_uti.cudaToNumpy(frame, width, height, 4)
    #frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame, str(round(fpsFilter, 1)) + ' fps ' + item, (0, 30), font, 1, (0, 0, 255), 2)
    #cv2.imshow('cam0', frame)
    cv2.imshow('cam1', frame)
    #cv2.moveWindow('cam1', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
    if KeyboardInterrupt is True:
        break

#cam0.release()
cam1.release()
cv2.destroyAllWindows()
