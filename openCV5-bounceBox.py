import cv2
print(cv2.__version__)


dispW = 1280
dispH = 720
flip = 0

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
bW = int(0.20 * dispW)
bH = int(0.15 * dispH)
posX = 10
posY = 270
dx = 10
dy = 10

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    cv2.moveWindow('nanoCam', 0, 10)
    frame = cv2.rectangle(frame, (posX, posY), (posX + bW, posY + bH), (255, 0, 0), -1)
    cv2.imshow('nanoCam',frame)
    posX = posX + dx
    posY = posY + dy

    if posX <= 0 or (posX + bW) >= dispW:
        dx = dx * (-1)

    if posY <= 0 or (posY + bH) >= dispH:
        dy = dy * (-1)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
