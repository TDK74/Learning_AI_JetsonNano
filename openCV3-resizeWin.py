import cv2
print(cv2.__version__)

dispW = 1280
dispH = 720
flip = 0
#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 700, 10)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frameSmall = cv2.resize(frame, (320, 240))
    graySmall = cv2.resize(gray, (320, 240))
    cv2.moveWindow('nanoSmall', 20, 0)
    cv2.moveWindow('bwSmall', 20, 265)
    cv2.imshow('nanoSmall', frameSmall)
    cv2.imshow('bwSmall', graySmall)

    cv2.moveWindow('nanoSmall2', 365, 0)
    cv2.moveWindow('bwSmall2', 365, 265)
    cv2.imshow('nanoSmall2', frameSmall)
    cv2.imshow('bwSmall2', graySmall)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
