import cv2
print(cv2.__version__)


dispW = 640
dispH = 480
flip = 0
bW = int(0.2 * dispW)
bH = int(0.2 * dispH)
posX = 10
posY = 270
dx = 2
dy = 2

#Uncomment These next Two Line for Pi Camera
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    roi = frame[posY:(posY + bH), posX:(posX + bW)].copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[posY:(posY + bH), posX:(posX + bW)] = roi
    cv2.rectangle(frame, (posX, posY), (posX + bW, posY + bH), (255, 0, 0), 3)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 10)
    posX = posX + dx
    posY = posY + dy

    if (posX + bW) >= dispW or posX <= 0:
        dx = dx * (-1)
    if (posY + bH) >= dispH or posY <= 0:
        dy = dy * (-1)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
