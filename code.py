from time import sleep
import board
import usb_hid
import digitalio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

btn_up = digitalio.DigitalInOut(board.GP18)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.DOWN

btn_down = digitalio.DigitalInOut(board.GP19)
btn_down.direction = digitalio.Direction.INPUT
btn_down.pull = digitalio.Pull.DOWN

btn_left = digitalio.DigitalInOut(board.GP14)
btn_left.direction = digitalio.Direction.INPUT
btn_left.pull = digitalio.Pull.DOWN

btn_right = digitalio.DigitalInOut(board.GP15)
btn_right.direction = digitalio.Direction.INPUT
btn_right.pull = digitalio.Pull.DOWN

btn_q = digitalio.DigitalInOut(board.GP12)
btn_q.direction = digitalio.Direction.INPUT
btn_q.pull = digitalio.Pull.DOWN

btn_enter = digitalio.DigitalInOut(board.GP13)
btn_enter.direction = digitalio.Direction.INPUT
btn_enter.pull = digitalio.Pull.DOWN

btn_r = digitalio.DigitalInOut(board.GP11)
btn_r.direction = digitalio.Direction.INPUT
btn_r.pull = digitalio.Pull.DOWN

btn_s = digitalio.DigitalInOut(board.GP10)
btn_s.direction = digitalio.Direction.INPUT
btn_s.pull = digitalio.Pull.DOWN

btn_t = digitalio.DigitalInOut(board.GP9)
btn_t.direction = digitalio.Direction.INPUT
btn_t.pull = digitalio.Pull.DOWN


while True:
    if btn_up.value:
        keyboard.press(Keycode.UP_ARROW)
        sleep(0.1)
        keyboard.release(Keycode.UP_ARROW)
    if btn_down.value:
        keyboard.press(Keycode.DOWN_ARROW)
        sleep(0.1)
        keyboard.release(Keycode.DOWN_ARROW)
    if btn_left.value:
        keyboard.press(Keycode.LEFT_ARROW)
        sleep(0.1)
        keyboard.release(Keycode.LEFT_ARROW)
    if btn_right.value:
        keyboard.press(Keycode.RIGHT_ARROW)
        sleep(0.1)
        keyboard.release(Keycode.RIGHT_ARROW)
    if btn_q.value:
        keyboard.press(Keycode.Q)
        sleep(0.1)
        keyboard.release(Keycode.Q)
    if btn_enter.value:
        keyboard.press(Keycode.ENTER)
        sleep(0.1)
        keyboard.release(Keycode.ENTER)
    if btn_r.value:
        keyboard.press(Keycode.R)
        sleep(0.1)
        keyboard.release(Keycode.R)
    if btn_s.value:
        keyboard.press(Keycode.S)
        sleep(0.1)
        keyboard.release(Keycode.S)
    if btn_t.value:
        keyboard.press(Keycode.T)
        sleep(0.1)
        keyboard.release(Keycode.T)
    sleep(0.1)




