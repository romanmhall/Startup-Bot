import menu_module
import ingame_module
import household_module
import time

def get_threshold():
    try:
        user_input = input("Enter minimum total trait score to keep campaign (e.g., 40): ")
        return int(user_input) if user_input.strip() else 40
    except ValueError:
        print("Invalid input. Defaulting to 40.")
        return 40

if __name__ == "__main__":
    threshold = get_threshold()
    attempt = 1

    while True:
        print(f"\nStarting automation loop attempt #{attempt}...\n")

        print("Waiting 5 seconds before starting menu sequence...")
        time.sleep(5)

        menu_module.run()
        ingame_module.run()

        success = household_module.run(threshold, attempt)

        if success:
            print("Campaign meets trait threshold. Loop complete.")
            break
        else:
            print("Trait score too low. Restarting sequence...\n")
            attempt += 1
            time.sleep(2)
