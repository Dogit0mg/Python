import time
import keyboard




time.sleep(5) #Wait 5 seconds to start the process
keyboard.press_and_release("windows+d") #Goes to desktop
time.sleep(1)
keyboard.press_and_release("alt+f4") #Opens the "turn off" window
time.sleep(1)
keyboard.press_and_release("enter") #Turns the computer off