import cv2
print(cv2.__version__)


def nothing(x):
    pass


cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue', 'Blended', 50, 100, nothing)

dispW = 320
dispH = 240
flip = 0

cvLogo = cv2.imread('/home/cuci/Documents/pyProg/cv.jpg')
cvLogo = cv2.resize(cvLogo, (320, 240))
cvLogoGray = cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('cvLogoGray', cvLogoGray)
cv2.moveWindow('cvLogoGray', 0, 280)

_, BGMask = cv2.threshold(cvLogoGray, 225, 255, cv2.THRESH_BINARY)
cv2.imshow('BGMask', BGMask)
cv2.moveWindow('BGMask', 330, 10)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask', FGMask)
cv2.moveWindow('FGMask', 330, 280)

FG = cv2.bitwise_and(cvLogo, cvLogo, mask = FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 660, 280)

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    BG = cv2.bitwise_and(frame, frame, mask = BGMask)
    cv2.imshow('BG', BG)
    cv2.moveWindow('BG', 660, 10)

    compImage = cv2.add(BG, FG)
    cv2.imshow('compImage', compImage)
    cv2.moveWindow('compImage', 990, 10)

    BV1 = cv2.getTrackbarPos('BlendValue', 'Blended') / 100
    BV2 = 1 - BV1

    Blended = cv2.addWeighted(frame, BV1, cvLogo, BV2, 0)
    cv2.imshow('Blended', Blended)
    cv2.moveWindow('Blended', 990, 280)

    FG2 = cv2.bitwise_and(Blended, Blended, mask = FGMask)
    cv2.imshow('FG2', FG2)
    cv2.moveWindow('FG2', 1320, 10)

    compFinal = cv2.add(BG, FG2)
    cv2.imshow('compFinal', compFinal)
    cv2.moveWindow('compFinal', 1320, 280)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 10)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
