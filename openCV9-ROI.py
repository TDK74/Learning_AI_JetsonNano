import cv2
print(cv2.__version__)


dispW = 640
dispH = 480
flip = 0

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    roi = frame[300:400, 360:470].copy()
    roiGray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray, cv2.COLOR_GRAY2BGR)
    #frame[300:400, 360:470] = [255, 255, 255]
    frame[300:400, 360:470] = roiGray
    cv2.imshow('nanoCam',frame)
    cv2.imshow('RoI', roi)
    cv2.imshow('Gray', roiGray)
    cv2.moveWindow('nanoCam', 0, 10)
    cv2.moveWindow('RoI', 645, 10)
    cv2.moveWindow('Gray', 645, 130)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
