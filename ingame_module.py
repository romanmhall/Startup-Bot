import time
import pyautogui

def run(threshold=None, attempt=None):
    click_positions = [
        (349, 429),
        (966, 1041),
        (1474, 905),
        (957, 763),
        (728, 468),
        (1474, 905),
        (949, 763)
    ]

    print("Running in-game click sequence...")

    for i, pos in enumerate(click_positions, start=1):
        print(f"Click {i} at {pos}")
        pyautogui.moveTo(pos)
        pyautogui.click()
        time.sleep(1)

    print("All clicks complete.")
    return True

if __name__ == "__main__":
    print("Running ingame_module standalone (test mode).")
    print("Starting in 5 seconds...")
    time.sleep(5)

    test_attempt = 1
    test_threshold = 0

    result = run(test_threshold, test_attempt)

    if result:
        print("Test run completed.")
    else:
        print("Test run exited campaign.")
