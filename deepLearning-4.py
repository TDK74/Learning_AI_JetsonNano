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

#Uncomment the next Line for Pi Camera
cam0 = jet_uti.gstCamera(width, height, '0')
#cam0 = jet_uti.gstCamera(width, height, '0', argv=['--input-flip=rotate-180'])  # not working

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam1 = jet_uti.gstCamera(width, height, '/dev/video1')
#cam2 = jet_uti.gstCamera(width, height, '/dev/video2')

net = jet_inf.imageNet('googlenet')
#'alexnet','googlenet-12','resnet-18','resnet-50','resnet-101','resnet-152','vgg-16','vgg-19','inception-v4'
font = cv2.FONT_HERSHEY_SIMPLEX
timeMark = time.time()
fpsFilter = 0

while True:
    frame, width, height = cam0.CaptureRGBA(zeroCopy=1)
    #frame, width, height = cam1.CaptureRGBA(zeroCopy=1)
    #frame, width, height = cam2.CaptureRGBA(zeroCopy=1)
    classID, confidence = net.Classify(frame, width, height)
    item = net.GetClassDesc(classID)
    dt = time.time() - timeMark
    fps = 1 / dt
    fpsFilter = 0.95*fpsFilter + 0.5*fps
    timeMark = time.time()
    frame = jet_uti.cudaToNumpy(frame, width, height, 4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame, str(round(fpsFilter, 1)) + ' fps ' + item, (0, 30), font, 1, (0, 0, 255), 2)
    cv2.imshow('cam0', frame)
    #cv2.imshow('cam1', frame)
    #cv2.imshow('cam2', frame)
    #cv2.moveWindow('cam0', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
    if KeyboardInterrupt is True:
        break

cam0.release()
#cam1.release()
#cam2.release()
cv2.destroyAllWindows()
