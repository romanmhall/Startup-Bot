# Startup-Bot

Video Demo: https://youtu.be/DmCm72CNmxg 

This project is a hands-on exploration of game automation, designed to interact with a strategy game's UI to test and log trait bonuses assigned to characters at the start of a new campaign. The primary motivation is to observe how certain in-game bonuses can combine—potentially up to a theoretical 120%—though results above 60% remain elusive. The script will loop automatically until a user-defined threshold is met, allowing long-term tracking of rare bonus configurations.

Even outside the scope of game-specific goals, the project showcases a practical application of Python automation with image recognition and UI interaction:

Screen Recognition with pyautogui
The scripts simulate real-time human interaction by locating UI elements on the screen using image matching. It uses reference images (e.g., trait tags like flirtatious_wife_text.png) to verify the presence of character traits with a confidence threshold.

Automated UI Sequences
menu_module.py and ingame_module.py simulate complex UI flows such as starting a new campaign or clicking through menus by defining click coordinates and timing delays, mimicking user behavior.

Trait Evaluation and Scoring
household_module.py identifies visible character traits and assigns predefined percentage scores to each one. It checks four household members by navigating to their positions and scanning trait regions.

Looping with Threshold Logic
The main.py loop continuously restarts the campaign if the total score from household traits doesn't meet the desired threshold, enabling the script to run unattended for long periods until ideal conditions are met.

Result Logging
Each run is timestamped and recorded into trait_results.csv, storing slot-specific trait values, total scores, and time taken. This makes it easy to analyze trends or visualize data over time.

This project can serve as a foundation or reference point for similar automation challenges involving UI testing, probabilistic simulations, or even light computer vision. Whether you're aiming to optimize game starts or just experimenting with automation pipelines, the codebase is modular and extensible for broader applications.

![image](https://github.com/user-attachments/assets/c353faa5-5476-47a5-a2e8-b54bb2776c10)
