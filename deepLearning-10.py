import cv2
print(cv2.__version__)


dispW = 640
dispH = 480
flip = 0

#Uncomment These next Two Line for Pi Camera
camSet = (' tcpclientsrc host=192.168.16.106 port=8554 ! gdpdepay ! rtph264depay ! h264parse ! nvv4l2decoder !'
          ' nvvidconv flip-method='+str(flip)+' ! video/x-raw,format=BGRx ! videoconvert !'
          ' video/x-raw, width='+str(dispW)+', height='+str(dispH)+',format=BGR ! appsink  drop=true sync=false ')
cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam = cv2.VideoCapture(1)

while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 10)

    if cv2.waitKey(1) == ord('q'):
        break

    if KeyboardInterrupt is True:
        break

cam.release()
cv2.destroyAllWindows()
