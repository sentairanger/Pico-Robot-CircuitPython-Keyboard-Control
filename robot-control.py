import curses
from gpiozero import CamJamKitRobot

torvalds = CamJamKitRobot()

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

curses.wrapper(main)
