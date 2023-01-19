import curses
from gpiozero import CamJamKitRobot, LED
import os
from time import sleep
from picamera import PiCamera
from datetime import datetime


torvalds = CamJamKitRobot()
eye = LED(25)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
moment = datetime.now()

eye.blink(n=4)

#Define the record and stop_record functions
def record():
    eye.off()
    camera.start_recording('/home/pi/Videos/video_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))

def stop_record():
    eye.on()
    camera.stop_recording()

actions = {
    curses.KEY_UP:    torvalds.right,
    curses.KEY_DOWN:  torvalds.left,
    curses.KEY_LEFT:  torvalds.forward,
    curses.KEY_RIGHT: torvalds.backward,
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            torvalds.stop()
        if key == ord('q'):
            break
        if key == ord('r'):
            record()
        if key == ord('s'):
            stop_record()
        if key == ord('t'):
            os.system('sudo shutdown now')

curses.wrapper(main)
eye.off()
torvalds.stop()
camera.stop_recording()