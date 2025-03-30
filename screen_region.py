import pyautogui
import time

# Size of the region box around the mouse (adjust as needed)
box_width = 300
box_height = 100

print("Move your mouse to the center of the target area...")
time.sleep(3)

mouse_x, mouse_y = pyautogui.position()
print(f"Mouse is at: ({mouse_x}, {mouse_y})")

# Calculate region from center point
left = mouse_x - box_width // 2
top = mouse_y - box_height // 2
region = (left, top, box_width, box_height)

print(f"Use this region: {region}")