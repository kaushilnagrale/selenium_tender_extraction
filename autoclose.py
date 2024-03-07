import time
import pyautogui

# Wait for a few seconds to give you time to focus on the PDF window
time.sleep(5)

# Set the coordinates of the close button (adjust these values based on your PDF viewer)
close_button_x = 305
close_button_y = 18

# Move the mouse to the close button and click
pyautogui.click(305, 18)

# You may need to adjust the sleep time based on your system's response time
time.sleep(2)
