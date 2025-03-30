import time
import pyautogui
import os

def run():
    image_folder = "rome_images"
    you_are_rome_image = os.path.join(image_folder, "you_are_rome.png")

    menu_clicks = [
        (31, 373),     # Hover Grand Campaign
        (213, 424),    # Click Grand Campaign
        (1018, 524),   # Click Faction
        (956, 966)     # Click Start Campaign
    ]

    loading_loop_positions = [
        (952, 1029),
        (939, 466)
    ]

    ingame_popup_region = None
    confidence_level = 0.7

    print("Running menu click sequence...")

    # Hover only on first position
    pyautogui.moveTo(menu_clicks[0])
    print(f"Hovering at {menu_clicks[0]}")
    time.sleep(1)

    # Click the remaining menu items with a short pause between each
    for i, pos in enumerate(menu_clicks[1:], start=2):
        print(f"Click {i} at {pos}")
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(1)

    print("Waiting for 'YOU ARE ROME' popup...")

    attempts = 0
    found = None

    while not found:
        try:
            found = pyautogui.locateOnScreen(you_are_rome_image, confidence=confidence_level, region=ingame_popup_region)
            if found:
                print("'YOU ARE ROME' popup detected.")
                break
        except pyautogui.ImageNotFoundException:
            pass

        # Perform looped interaction while waiting
        for pos in loading_loop_positions:
            pyautogui.moveTo(pos)
            pyautogui.click()
            time.sleep(0.5)

        attempts += 1
        if attempts % 10 == 0:
            print("Still waiting for image...")

    print("Menu and campaign load complete.")
    return True

if __name__ == "__main__":
    print("Running menu_module standalone (test mode).")
    print("Starting in 5 seconds...")
    time.sleep(5)
    run()
