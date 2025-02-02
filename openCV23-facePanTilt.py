import cv2
print(cv2.__version__)
from adafruit_servokit import ServoKit


dispW = 640
dispH = 480
flip = 0

kit = ServoKit(channels=16)
pan = 90
tilt = 140
kit.servo[0].angle = pan
kit.servo[1].angle = tilt

#Uncomment These next Two Line for Pi Camera
#camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(flip) +' ! video/x-raw, width='+ str(dispW) +', height='+ str(dispH) +', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam = cv2.VideoCapture(1)
cam.set(3, dispW)
cam.set(4, dispH)

face_cascade = cv2.CascadeClassifier("/home/your_user_name/Documents/pyProg/cascade/face.xml")
#profile_cascade = cv2.CascadeClassifier("/home/your_user_name/Documents/pyProg/cascade/profile.xml")
eye_cascade = cv2.CascadeClassifier("/home/your_user_name/Documents/pyProg/cascade/eye.xml")
#bodyup_cascade = cv2.CascadeClassifier("/home/your_user_name/Documents/pyProg/cascade/bodyup.xml")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #profi_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #profiles = profile_cascade.detectMultiScale(profi_gray)
    #bodyUp = bodyup_cascade.detectMultiScale(gray)

    #for (x, y, w, h) in zip(faces, profiles):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        xCent = x + w/2
        yCent = y + h/2
        errorPan = xCent - dispW/2
        errorTilt = yCent - dispH/2

        if abs(errorPan) > 15:
            pan = pan - errorPan/30
        if abs(errorTilt) > 15:
            tilt = tilt - errorTilt/30
        if pan > 180:
            pan = 180
            print('Pan out of range!!!')
        if pan < 0:
            pan = 0
            print('Pan out of range!!!')
        if tilt > 180:
            tilt = 180
            print('Tilt out of range!!!')
        if tilt < 0:
            tilt = 0
            print('Tilt out of range!!!')

        kit.servo[0].angle = pan
        kit.servo[1].angle = tilt
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (xEye, yEye, wEye, hEye) in eyes:
            cv2.rectangle(roi_color, (xEye, yEye), (xEye+wEye, yEye+hEye), (255, 0, 0), 2)
            #cv2.circle(roi_color, (int(xEye+wEye/2), int(yEye+hEye/2)), 24, (255, 0, 0), 2)

        break

    cv2.imshow('nanoCam',frame)
    #cv2.moveWindow('nanoCam', 300, 200)
    #cv2.moveWindow('nanoCam', 300, 180) # uncomment for a web camera

    if cv2.waitKey(1) == ord('q'):
        break
    if KeyboardInterrupt is True:
        break

cam.release()
cv2.destroyAllWindows()
