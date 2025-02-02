import cv2
print(cv2.__version__)

dispW = 640
dispH = 480
flip = 0

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

PL = cv2.imread('/home/your_user_name/Documents/pyProg/pl.jpg')
PL = cv2.resize(PL, (85, 85))
cv2.imshow('LogoWindow', PL)
cv2.moveWindow('LogoWindow', 650, 10)

PLGray = cv2.cvtColor(PL, cv2.COLOR_BGR2GRAY)
cv2.imshow('LGGray', PLGray)
cv2.moveWindow('LGGray', 750, 10)

_, BGMask = cv2.threshold(PLGray, 245, 255, cv2.THRESH_BINARY)
cv2.imshow('BGMask', BGMask)
cv2.moveWindow('BGMask', 850, 10)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask', FGMask)
cv2.moveWindow('FGMask', 950, 10)

FG = cv2.bitwise_and(PL, PL, mask = FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 1050, 10)

bW = 85
bH = 85
posX = 10
posY = 10
dx = 1
dy = 1

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()

    RoI = frame[posY:posY + bH, posX:posX + bW]
    RoIBG = cv2.bitwise_and(RoI, RoI, mask = BGMask)
    cv2.imshow('RoIBG', RoIBG)
    cv2.moveWindow('RoIBG', 1150, 10)

    RoInew = cv2.add(FG, RoIBG)
    cv2.imshow('RoInew', RoInew)
    cv2.moveWindow('RoInew', 1250, 10)
    frame[posY:posY + bH, posX:posX + bW] = RoInew

    posX = posX + dx
    posY = posY + dy

    if posX <= 0 or (posX + bW) >= dispW:
        dx = dx * (-1)

    if posY <= 0 or (posY + bH) >= dispH:
        dy = dy * (-1)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 10)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
