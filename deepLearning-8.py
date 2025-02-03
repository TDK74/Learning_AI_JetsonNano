import cv2
import jetson_inference as jet_inf
import jetson_utils as jet_uti
import time
import numpy as np


net = jet_inf.imageNet('vgg-16',
            ['--model=/home/cuci/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx',
            '--input_blob=input_0', '--output_blob=output_0',
            '--labels=/home/cuci/Downloads/jetson-inference/myTrain/labels.txt'])
#'alexnet','googlenet','googlenet-12','resnet-18','resnet-50',
#'resnet-101','resnet-152','vgg-16','vgg-19','inception-v4'

width = int(640 * 1)
height = int(480 * 1)
dispW = width
dispH = height
flip = 0

#Uncomment These next Two Line for Pi Camera
""" camSet = ('nvarguscamerasrc wbmode=9 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !'
          ' video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 !'
          ' nvvidconv flip-method='+ str(flip) +' !'
          ' video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx !'
          ' videoconvert ! video/x-raw, format=BGR !'
          ' videobalance contrast=1.5 brightness=-0.2 saturation=1.2 ! appsink drop=1')
cam0 = cv2.VideoCapture(camSet) """

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam1 = cv2.VideoCapture('/dev/video1')
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, dispW) # or cam1.set(3, dispW)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH) # or cam1.set(4, dispW)
#cam2 = cv2.VideoCapture('/dev/video2')
#cam2.set(cv2.CAP_PROP_FRAME_WIDTH, dispW) # or cam2.set(3, dispW)
#cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH) # or cam2.set(4, dispW)

font = cv2.FONT_HERSHEY_SIMPLEX
timeMark = time.time()
fpsFilter = 0

while True:
    #_, frame = cam0.read()
    _, frame = cam1.read()
    #_, frame = cam2.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jet_uti.cudaFromNumpy(img)
    classID, confidence = net.Classify(img, width, height)
    item = net.GetClassDesc(classID)
    dt = time.time() - timeMark
    fps = 1 / dt
    fpsFilter = 0.95*fpsFilter + 0.5*fps
    timeMark = time.time()
    cv2.putText(frame, str(round(fpsFilter, 1)) + ' fps ' + item, (0, 30), font, 1, (0, 0, 255), 2)
    #cv2.imshow('cam0', frame)
    cv2.imshow('cam1', frame)
    #cv2.imshow('cam2', frame)
    #cv2.moveWindow('cam0', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
    if KeyboardInterrupt is True:
        break

#cam0.release()
cam1.release()
#cam2.release()
cv2.destroyAllWindows()
