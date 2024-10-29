import time
import keyboard
import win32api
import win32con

CENTER = (1243, 533) # two skills requires you to aim, so we need the center position to aim them
click_positions = [
    (631, 330), (702, 330), (772, 330),
    (631, 412), (702, 412), (772, 412),
    (631, 494), CENTER, (702, 494), CENTER,
    (772, 494), (631, 576), (702, 576),
    (772, 576)
]

def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)  # 0.01-second delay before left click to avoid errors in the click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.06) # 0.06-second delay before "mouse left up" to avoid errors in click detection
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def Use_skills():
    paused = False # initialize the paused variable
    while not keyboard.is_pressed("q"): # if the "q" button is not pressed -> continue
        # Check for pause toggle
        if keyboard.is_pressed("up"): # if the "up arrow" key is pressed -> continue
            paused = not paused # inverts the value of "paused", if it's negative it turns positive, and vice-versa
            time.sleep(0.3)  # Small delay to avoid rapid toggling

        
        while paused: # while "paused" == True
            if keyboard.is_pressed("up"): # if the "up arrow" key is pressed -> "paused" == False and break the loop
                paused = False
                time.sleep(0.3)  # Small delay to avoid rapid toggling
                break

        # Perform click sequence if not paused
        if not paused:
            for pos in click_positions:
                click(*pos) # have to use "*" to cast into a tuple for some reason

# 5 seconds delay before starting to have enough time to switch apps
time.sleep(5)
Use_skills()