import cv2
print(cv2.__version__)

dispW = 640
dispH = 480
flip = 0
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=29/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
piCam = cv2.VideoCapture(camSet)
usbCam = cv2.VideoCapture(1)

while True:
    ret, frame = piCam.read()
    ret, frame2 = usbCam.read()
    cv2.imshow('PiCam', frame)
    cv2.imshow('UsbCam', frame2)

    if cv2.waitKey(1) == ord('q'):
        break

piCam.release()
usbCam.release()
cv2.destroyAllWindows()
