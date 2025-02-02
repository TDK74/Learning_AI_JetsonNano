from threading import Thread
import time

def BigBox(color, lng) -> None:
    while True:
        print('Big', color, 'box is open', lng)
        time.sleep(5)
        print('Big', color, 'box is closed', lng)
        time.sleep(5)

        if KeyboardInterrupt is True:
            break

def SmallBox(color, lng) -> None:
    while True:
        print('Small', color, 'box is open', lng)
        time.sleep(1)
        print('Small', color, 'box is closed', lng)
        time.sleep(1)

        if KeyboardInterrupt is True:
            break


bigBoxThread = Thread(target=BigBox, args=('red', 4))
smallBoxThread = Thread(target=SmallBox, args=('blue', 5))
bigBoxThread.daemon = True
smallBoxThread.daemon = True
bigBoxThread.start()
smallBoxThread.start()

while True:
    pass
