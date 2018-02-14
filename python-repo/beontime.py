import time
import pyautogui

x=0
y=700
for i in range(1000):
    pyautogui.moveTo(x,y,duration=1)
    pyautogui.click(x,y)
    time.sleep(2)
    x,y=y,x

#11. Listening to keyboard infinite time, stops when perticular key is pressed

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


import time
import pyautogui

x=0
y=700
for i in range(1000):
    pyautogui.moveTo(x,y,duration=1)
    pyautogui.click(x,y)
    time.sleep(2)
    x,y=y,x





import time
import pyautogui
from pynput import keyboard

def on_press(key):
    x=0
    y=700
    for i in range(1000):
        pyautogui.moveTo(x,y,duration=1)
        pyautogui.click(x,y)
        time.sleep(2)
        x,y=y,x

def on_release(key):
    x=0
    y=700
    for i in range(1000):
        pyautogui.moveTo(x,y,duration=1)
        pyautogui.click(x,y)
        time.sleep(2)
        x,y=y,x
        if key == keyboard.Key.esc:
            # Stop listener
            return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()