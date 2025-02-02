import RPi.GPIO as Gpio
import time


inPin = 15
outPin = 23
LedState = False
btnStateOld = True

Gpio.cleanup()
Gpio.setmode(Gpio.BOARD)
Gpio.setup(inPin, Gpio.IN)
Gpio.setup(outPin, Gpio.OUT)

while True:
    btnStateNew = Gpio.input(inPin)
    #if btnStateOld is False and btnStateNew is True:
    if btnStateOld is True and btnStateNew is False:
        LedState is not LedState

    Gpio.output(outPin, LedState)
    inLvl = Gpio.input(inPin)
    print(f'The status of pin {inPin} is {inLvl}')
    time.sleep(1)

    if KeyboardInterrupt is True:
        break

Gpio.cleanup()
