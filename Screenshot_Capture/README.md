# Capture Screenshot
captures screenshot at regular interval of time.


### Tech Stack:
+ Python

### Libraries:
+ os
+ argparse
+ time
+ pyautogui

### Pre requirements:
+ Install requirements.txt `pip install -r requirements.txt`

### To execute the project/play:
```bash
python screenshot.py                          # takes screenshot at interval of 1 hour
python screenshot.py -t m -f 5                # takes 5 screenshots in 1 minute 
python screenshot.py -p path_to_directory     # screenshots will be saved to path_to_directory
```