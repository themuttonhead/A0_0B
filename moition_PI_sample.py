from gpiozero import MotionSensor
import os
import time
PIR=MotionSensor(4)
if PIR.motion_detected:
    time.sleep(2)
    print("motion")
    os.system( "fswebcam -F 5 --fps 20  -r 800x600 /home/pi/13.jpg " )
    print("pic taken")
else:
    print("no")
