import jetson_inference as jet_inf
import jetson_utils as jet_uti
import time
#import cv2


width = int(640 * 2)
height = int(480 * 1.5)
dispW = width
dispH = height
timeStamp = time.time()
fpsFltr = 0

net = jet_inf.detectNet('ssd-mobilenet-v2', threshold=0.5)
#'ssd-mobilenet-v1','ssd-inception-v2','peoplenet','peoplenet-pruned','dashcamnet','trafficcamnet','facedetect'

cam0 = jet_uti.gstCamera(dispW, dispH, '0')
#cam1 = jet_uti.gstCamera(dispW, dispH, '/dev/video1')
#cam2 = jet_uti.gstCamera(dispW, dispH, '/dev/video2')
display = jet_uti.glDisplay()

while display.IsOpen():
    img, width, height = cam0.CaptureRGBA()
    #img, width, height = cam1.CaptureRGBA()
    #img, width, height = cam2.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    dt = time.time() - timeStamp
    timeStamp = time.time()
    fps = 1 / dt
    fpsFltr = 0.9*fpsFltr + 0.1*fps
    print(str(round(fps, 1)) + ' fps ')
