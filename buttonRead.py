import RPi.GPIO as GPIO
import time


inPin = 15

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

while True:
    inp = GPIO.input(15)
    time.sleep(1)
    print("The level on pin is: ", inp)

    if KeyboardInterrupt is True:
        break

GPIO.cleanup(15)
GPIO.cleanup()
