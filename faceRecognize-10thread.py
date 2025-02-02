from threading import Thread
import time

def BigBox() -> None:
    while True:
        print('Big box is open')
        time.sleep(5)
        print('Big box is closed')
        time.sleep(5)

        if KeyboardInterrupt is True:
            break

def SmallBox() -> None:
    while True:
        print('Small box is open')
        time.sleep(1)
        print('Small box is closed')
        time.sleep(1)

        if KeyboardInterrupt is True:
            break

#BigBox()
#SmallBox()

bigBoxThread = Thread(target=BigBox, args=())
smallBoxThread = Thread(target=SmallBox, args=())
bigBoxThread.daemon = True
smallBoxThread.daemon = True
bigBoxThread.start()
smallBoxThread.start()

while True:
    pass
