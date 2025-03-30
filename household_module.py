import time
import pyautogui
import csv
import os
from datetime import datetime

def run(score_threshold, attempt_num):
    trait_scores = {
        'fertile_wife': 30,
        'beautiful_wife': 10,
        'flirtatious_wife': 5,
        'flirtatious_husband': 5,
        'faithful_wife': 5,
        'domestic_goddess': 5,
        'prolific_husband': 30,
        'gifted_husband': 20,
        'faithful_husband': 10
    }

    image_folder = "rome_images"
    trait_region = (1100, 800, 500, 300)

    click_positions = [
        (679, 465),
        (772, 475),
        (970, 470),
        (1065, 473)
    ]
    hover_position = (1160, 807)

    exit_sequence = [
        (951, 980),
        (29, 15),
        (956, 551),
        (921, 494)
    ]

    csv_file = "trait_results.csv"
    csv_headers = ['Attempt', 'Date', 'Slot 1', 'Slot 2', 'Slot 3', 'Slot 4', 'Total', 'Time']

    total_score = 0
    slot_scores = []
    start_time = time.time()

    for i, click_pos in enumerate(click_positions, start=1):
        print(f"\nSlot {i}: Click at {click_pos}, hover at {hover_position}")
        pyautogui.moveTo(click_pos)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(hover_position)
        time.sleep(2)

        found = False
        slot_score = 0

        print(f"Scanning region {trait_region}...")

        for trait_base, score in trait_scores.items():
            text_path = os.path.join(image_folder, f"{trait_base}_text.png")
            tag_path = os.path.join(image_folder, f"{trait_base}_tag.png")

            print(f"Checking {trait_base}...")

            try:
                text_found = pyautogui.locateOnScreen(text_path, confidence=0.7, region=trait_region)
                if text_found:
                    print(f"Text match for {trait_base}")

                    tag_found = pyautogui.locateOnScreen(tag_path, confidence=0.7, region=trait_region)
                    if tag_found:
                        print(f"Tag confirmed for {trait_base} (+{score}%)")
                        total_score += score
                        slot_score = score
                        found = True
                        break
                    else:
                        print(f"Tag not found for {trait_base} (possible false match)")
            except pyautogui.ImageNotFoundException:
                pass
            except ValueError as e:
                print(f"Error with {trait_base}: {e}")

        if not found:
            print("No traits found for this slot.")

        slot_scores.append(slot_score)

    elapsed_time = round(time.time() - start_time, 2)
    current_date = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    attempt_label = f"Attempt {attempt_num} ({score_threshold}%)"
    row = [attempt_label, current_date] + slot_scores + [total_score, elapsed_time]

    write_headers = True
    if os.path.exists(csv_file):
        with open(csv_file, 'r', newline='') as check_file:
            if check_file.readline().strip().startswith('Attempt'):
                write_headers = False

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if write_headers:
            writer.writerow(csv_headers)
        writer.writerow(row)

    print(f"\nLogged result to {csv_file}")
    print(f"Total trait score: {total_score}% (Threshold: {score_threshold}%)")
    print(f"Time taken: {elapsed_time} seconds")

    if total_score >= score_threshold:
        print("Threshold met. Keeping campaign.")
        return True
    else:
        print("Trait score too low. Exiting to main menu.")
        for i, pos in enumerate(exit_sequence, start=1):
            print(f"Exit Click {i} at {pos}")
            pyautogui.moveTo(pos)
            pyautogui.click()
            time.sleep(1)

        print("Household trait check complete.")
        return False

if __name__ == "__main__":
    print("Running household_module standalone (test mode).")
    print("Starting in 5 seconds...")
    time.sleep(5)

    test_attempt = 1
    test_threshold = 0

    result = run(test_threshold, test_attempt)

    if result:
        print("Test run completed.")
    else:
        print("Test run exited campaign.")
